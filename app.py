from flask import Flask, render_template, request
import pdfplumber
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_first_mcq(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    pattern = re.compile(
        r"\d+\.\s*(.*?)\n"
        r"\(a\)\s*(.*?)\n"
        r"\(b\)\s*(.*?)\n"
        r"\(c\)\s*(.*?)\n"
        r"\(d\)\s*(.*?)\n",
        re.DOTALL
    )

    match = pattern.search(text)

    if match:
        return {
            "question": match.group(1).strip(),
            "a": match.group(2).strip(),
            "b": match.group(3).strip(),
            "c": match.group(4).strip(),
            "d": match.group(5).strip(),
        }

    return None


@app.route("/", methods=["GET", "POST"])
def index():
    mcq = None

    if request.method == "POST":
        pdf = request.files.get("pdf")
        if pdf:
            file_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
            pdf.save(file_path)
            mcq = extract_first_mcq(file_path)

    return render_template("index.html", mcq=mcq)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

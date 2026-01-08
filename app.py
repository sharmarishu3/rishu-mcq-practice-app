from flask import Flask, render_template, request
import pdfplumber
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_first_mcq(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

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
            "question": match.group(1),
            "a": match.group(2),
            "b": match.group(3),
            "c": match.group(4),
            "d": match.group(5)
        }

    return None


@app.route("/", methods=["GET", "POST"])
def index():
    mcq = None

    if request.method == "POST":
        pdf = request.files["pdf"]
        path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(path)

        mcq = extract_first_mcq(path)

    return render_template("index.html", mcq=mcq)


if __name__ == "__main__":
    app.run(debug=True)

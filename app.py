from flask import Flask, render_template, request
import pdfplumber
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def extract_mcqs(text):
    mcqs = []

    # Question pattern (1. question)
    question_blocks = re.split(r"\n\s*\d+\.\s*", text)

    for block in question_blocks[1:3]:  # sirf 1–2 MCQ test ke liye
        lines = block.strip().split("\n")

        question = lines[0]

        options = []
        for line in lines[1:]:
            if re.match(r"\([a-d]\)", line.lower()):
                options.append(line)

        if len(options) >= 4:
            mcqs.append({
                "question": question,
                "options": options[:4]
            })

    return mcqs


@app.route("/", methods=["GET", "POST"])
def home():
    mcqs = []

    if request.method == "POST":
        pdf = request.files.get("pdf")
        if pdf:
            pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
            pdf.save(pdf_path)

            full_text = ""
            with pdfplumber.open(pdf_path) as pdf_file:
                for page in pdf_file.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"

            mcqs = extract_mcqs(full_text)

    return render_template("index.html", mcqs=mcqs)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

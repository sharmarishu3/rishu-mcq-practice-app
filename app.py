from flask import Flask, render_template, request, redirect, url_for
import os
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Temporary MCQs (jab tak PDF se auto extract nahi karte)
questions = [
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["दिल्ली", "मुंबई", "चेन्नई", "कोलकाता"],
        "answer": "दिल्ली"
    },
    {
        "question": "गुजरात की राजधानी क्या है?",
        "options": ["सूरत", "राजकोट", "गांधीनगर", "अहमदाबाद"],
        "answer": "गांधीनगर"
    },
    {
        "question": "20वीं सदी का सबसे बड़ा युद्ध कौन सा था?",
        "options": ["प्रथम विश्व युद्ध", "द्वितीय विश्व युद्ध", "शीत युद्ध", "कोई नहीं"],
        "answer": "द्वितीय विश्व युद्ध"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    pdf = request.files.get("pdf")
    if not pdf:
        return "No PDF uploaded"

    path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
    pdf.save(path)

    # PDF text read (Phase 2 base)
    text = ""
    with pdfplumber.open(path) as pdf_file:
        for page in pdf_file.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"

    # Abhi sirf test ke liye MCQ dikha rahe
    return redirect(url_for("quiz"))

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

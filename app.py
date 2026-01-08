from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# TEMP MCQs (PDF logic baad me add hoga)
QUESTIONS = [
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["दिल्ली", "मुंबई", "चेन्नई", "कोलकाता"],
        "answer": "दिल्ली"
    },
    {
        "question": "गुजरात की राजधानी क्या है?",
        "options": ["सूरत", "राजकोट", "गांधीनगर", "अहमदाबाद"],
        "answer": "गांधीनगर"
    }
]

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "pdf" not in request.files:
        return "No file uploaded"

    pdf = request.files["pdf"]
    if pdf.filename == "":
        return "No selected file"

    path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
    pdf.save(path)

    return redirect(url_for("quiz"))

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=QUESTIONS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

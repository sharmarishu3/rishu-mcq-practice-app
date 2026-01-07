from flask import Flask, render_template, request, redirect
import os
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# TEMP questions (PDF parse hone ke baad replace ho jayega)
questions = [
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["दिल्ली", "मुंबई", "चेन्नई", "कोलकाता"],
        "answer": "दिल्ली"
    }
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "pdf" not in request.files:
        return "No file uploaded"

    pdf = request.files["pdf"]
    if pdf.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
    pdf.save(filepath)

    # ===== PDF TEXT READ =====
    text = ""
    with pdfplumber.open(filepath) as pdf_file:
        for page in pdf_file.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    # 🔴 अभी सिर्फ text print होगा (Render logs में दिखेगा)
    print("===== PDF TEXT START =====")
    print(text)
    print("===== PDF TEXT END =====")

    # बाद में यही text parse करेंगे
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





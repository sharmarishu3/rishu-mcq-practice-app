from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_pdf():
    if request.method == "POST":
        pdf = request.files.get("pdf")
        if pdf:
            pdf.save(os.path.join(UPLOAD_FOLDER, pdf.filename))
            return "PDF uploaded successfully! (MCQ reading next step)"
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

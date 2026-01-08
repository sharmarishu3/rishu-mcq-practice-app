from flask import Flask, render_template, request
import pdfplumber
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    pdf_text = ""

    if request.method == "POST":
        pdf = request.files.get("pdf")
        if pdf:
            pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf.filename)
            pdf.save(pdf_path)

            # 🔹 PDF READ START
            with pdfplumber.open(pdf_path) as pdf_file:
                for page in pdf_file.pages:
                    text = page.extract_text()
                    if text:
                        pdf_text += text + "\n\n"

    return render_template("index.html", pdf_text=pdf_text)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

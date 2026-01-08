from flask import Flask, render_template, request, redirect, session
import os
import random
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = "mcq_secret_key"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------- PDF MCQ EXTRACT (BASIC) --------
def extract_mcqs_from_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    lines = [l.strip() for l in text.split("\n") if l.strip()]

    mcqs = []
    i = 0
    while i < len(lines) - 5:
        if lines[i][0].isdigit() and "." in lines[i]:
            question = lines[i]
            options = lines[i+1:i+5]

            if all(o.startswith(("a", "b", "c", "d", "(")) for o in options):
                mcqs.append({
                    "question": question,
                    "options": options,
                    "answer": options[0]  # TEMP (answer key later)
                })
                i += 5
            else:
                i += 1
        else:
            i += 1

    return mcqs

# -------- ROUTES --------

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        pdf = request.files["pdf"]
        if not pdf:
            return "No file uploaded"

        path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(path)

        mcqs = extract_mcqs_from_pdf(path)

        session["all_mcqs"] = mcqs
        return redirect("/start")

    return render_template("upload.html")


@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        count = int(request.form["count"])
        mcqs = session.get("all_mcqs", [])

        random.shuffle(mcqs)
        session["quiz"] = mcqs[:count]
        session["index"] = 0
        session["score"] = 0

        return redirect("/quiz")

    return render_template("upload.html", step="select")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    quiz = session.get("quiz", [])
    index = session.get("index", 0)

    if index >= len(quiz):
        return render_template(
            "quiz.html",
            finished=True,
            score=session["score"],
            total=len(quiz)
        )

    if request.method == "POST":
        selected = request.form.get("option")
        correct = quiz[index]["answer"]

        if selected == correct:
            session["score"] += 1

        session["index"] += 1
        return redirect("/quiz")

    return render_template(
        "quiz.html",
        q=quiz[index],
        index=index + 1,
        total=len(quiz),
        finished=False
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

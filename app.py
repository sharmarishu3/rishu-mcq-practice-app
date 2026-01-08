from flask import Flask, render_template, request, redirect, session
import os, random, re
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = "final_secret"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_mcqs(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"

    lines = [l.strip() for l in text.split("\n") if l.strip()]
    mcqs = []
    answers = {}

    for line in lines:
        m = re.match(r"(\d+)\s*[:\.\-]?\s*([a-dA-D])$", line)
        if m:
            answers[m.group(1)] = m.group(2).lower()

    i = 0
    while i < len(lines):
        q = re.match(r"(\d+)[\.\)]\s*(.+)", lines[i])
        if q:
            qno = q.group(1)
            question = q.group(2)
            options = []
            j = i + 1

            while j < len(lines) and len(options) < 4:
                if re.match(r"[\(\[]?[a-dA-D][\)\]]", lines[j]):
                    options.append(lines[j])
                j += 1

            if len(options) == 4 and qno in answers:
                idx = ord(answers[qno]) - ord("a")
                if 0 <= idx < 4:
                    mcqs.append({
                        "question": question,
                        "options": options,
                        "answer": options[idx]
                    })
            i = j
        else:
            i += 1

    return mcqs

@app.route("/", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        pdf = request.files.get("pdf")
        count = request.form.get("count")

        path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(path)

        mcqs = extract_mcqs(path)
        if not mcqs:
            return "No MCQs found in PDF"

        random.shuffle(mcqs)
        if count != "all":
            mcqs = mcqs[:int(count)]

        session["mcqs"] = mcqs
        session["index"] = 0
        session["score"] = 0

        return redirect("/quiz")

    return render_template("upload.html")

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    mcqs = session.get("mcqs")
    if not mcqs:
        return redirect("/")

    idx = session["index"]

    if request.method == "POST":
        if request.form["option"] == mcqs[idx]["answer"]:
            session["score"] += 1
        session["index"] += 1
        idx += 1

    if idx >= len(mcqs):
        total = len(mcqs)
        correct = session["score"]
        return render_template(
            "quiz.html",
            finished=True,
            total=total,
            correct=correct,
            wrong=total-correct,
            accuracy=round(correct*100/total,2)
        )

    return render_template(
        "quiz.html",
        q=mcqs[idx],
        index=idx+1,
        total=len(mcqs),
        finished=False
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)

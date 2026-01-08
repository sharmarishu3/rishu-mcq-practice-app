from flask import Flask, render_template, request, redirect, session
import os, random, re
import pdfplumber

app = Flask(__name__)
app.secret_key = "final_mcq_secret"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_mcqs(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"

    lines = [l.strip() for l in text.split("\n") if l.strip()]
    mcqs = []
    answers = {}

    # answer key detect
    for line in lines:
        m = re.match(r"(\d+)\s*[\.\-:]?\s*([a-dA-D])", line)
        if m:
            answers[m.group(1)] = m.group(2).lower()

    i = 0
    while i < len(lines):
        q_match = re.match(r"(\d+)[\.\)]\s*(.*)", lines[i])
        if q_match:
            qno = q_match.group(1)
            question = q_match.group(2)
            options = []
            j = i + 1
            while j < len(lines) and len(options) < 4:
                if re.match(r"[\(\[]?[a-dA-D][\)\]]", lines[j]):
                    options.append(lines[j])
                j += 1

            if len(options) == 4 and qno in answers:
                correct_index = ord(answers[qno]) - ord("a")
                mcqs.append({
                    "question": question,
                    "options": options,
                    "answer": options[correct_index]
                })
            i = j
        else:
            i += 1

    return mcqs

@app.route("/", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        pdf = request.files["pdf"]
        count = request.form["count"]
        path = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(path)

        mcqs = extract_mcqs(path)
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
    mcqs = session["mcqs"]
    idx = session["index"]

    if request.method == "POST":
        selected = request.form["option"]
        if selected == mcqs[idx]["answer"]:
            session["score"] += 1
        session["index"] += 1
        idx += 1

    if idx >= len(mcqs):
        total = len(mcqs)
        correct = session["score"]
        wrong = total - correct
        accuracy = round((correct/total)*100,2)
        return render_template("quiz.html",
            finished=True,
            correct=correct,
            wrong=wrong,
            total=total,
            accuracy=accuracy)

    return render_template("quiz.html",
        q=mcqs[idx],
        index=idx+1,
        total=len(mcqs),
        finished=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)

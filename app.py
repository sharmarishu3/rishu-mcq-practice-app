from flask import Flask, render_template, request, jsonify
import pdfplumber
import re
import random

app = Flask(__name__)

questions = []
answers = {}
quiz = []
index = 0
score = 0

def extract_text(pdf):
    text = ""
    with pdfplumber.open(pdf) as p:
        for page in p.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def parse_mcqs(text):
    qs = []
    blocks = re.split(r'\n\d+\.', text)
    for b in blocks:
        lines = [l.strip() for l in b.split("\n") if l.strip()]
        if len(lines) >= 5:
            qs.append({
                "q": lines[0],
                "opts": lines[1:5]
            })
    return qs

def parse_answers(text):
    ans = {}
    for line in text.splitlines():
        m = re.search(r'(\d+)\s*[:\-]\s*([abcdABCD])', line)
        if m:
            ans[int(m.group(1))-1] = m.group(2).lower()
    return ans

@app.route("/", methods=["GET", "POST"])
def home():
    global questions, answers, quiz, index, score
    if request.method == "POST":
        mcq_pdf = request.files["mcq"]
        ans_pdf = request.files["ans"]
        limit = request.form["limit"]

        questions = parse_mcqs(extract_text(mcq_pdf))
        answers = parse_answers(extract_text(ans_pdf))

        random.shuffle(questions)

        if limit != "all":
            questions = questions[:int(limit)]

        quiz = questions
        index = 0
        score = 0

        return render_template("quiz.html")

    return render_template("index.html")

@app.route("/question")
def question():
    global index
    if index >= len(quiz):
        return jsonify({"done": True})

    q = quiz[index]
    return jsonify({
        "no": index + 1,
        "total": len(quiz),
        "q": q["q"],
        "opts": q["opts"]
    })

@app.route("/answer", methods=["POST"])
def answer():
    global index, score
    data = request.json
    selected = data["selected"]
    correct = answers.get(index)

    right = selected == correct
    if right:
        score += 1

    index += 1

    return jsonify({"right": right})

@app.route("/result")
def result():
    total = len(quiz)
    return jsonify({
        "total": total,
        "correct": score,
        "wrong": total-score,
        "accuracy": round((score/total)*100, 2)
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)





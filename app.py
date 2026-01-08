from flask import Flask, render_template
import os

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "ભારતની રાજધાની શું છે?",
        "options": ["દિલ્લી", "મુંબઈ", "ચેન્નઈ", "કોલકાતા"],
        "answer": "દિલ્લી"
    },
    {
        "question": "Gujarat ni rajdhani shu chhe?",
        "options": ["Surat", "Rajkot", "Gandhinagar", "Ahmedabad"],
        "answer": "Gandhinagar"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Sun rises in the?",
        "options": ["North", "South", "East", "West"],
        "answer": "East"
    }
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

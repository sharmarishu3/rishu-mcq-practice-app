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
        "options": ["દિલ્લી", "મુંબઇ", "ચેન્નઈ", "કોલકાતા"],
        "answer": "દિલ્લી"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




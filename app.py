from flask import Flask, render_template

app = Flask(__name__)
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "ભારતની રાજધાની શું છે?",
        "options": ["દિલ્લી", "મુંબઇ", "ચેન્નાઈ", "કોલકાતા"],
        "answer": "દિલ્લી"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


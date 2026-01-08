from flask import Flask, render_template
import os

app = Flask(__name__)

questions = [
    {
        "question": "20वीं सदी का सबसे बड़ा युद्ध कौन सा था?",
        "options": ["प्रथम विश्व युद्ध", "द्वितीय विश्व युद्ध", "शीत युद्ध", "कोई नहीं"],
        "answer": "द्वितीय विश्व युद्ध"
    },
    {
        "question": "भारत की राजधानी क्या है?",
        "options": ["दिल्ली", "मुंबई", "चेन्नई", "कोलकाता"],
        "answer": "दिल्ली"
    },
    {
        "question": "गुजरात की राजधानी क्या है?",
        "options": ["सूरत", "राजकोट", "गांधीनगर", "अहमदाबाद"],
        "answer": "गांधीनगर"
    }
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

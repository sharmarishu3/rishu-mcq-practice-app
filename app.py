from flask import Flask, render_template
import os

app = Flask(__name__)

questions = [

    # ---------- ENGLISH MCQs (10) ----------
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who is the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Subhash Bose", "Mahatma Gandhi", "Bhagat Singh"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "2 + 5 = ?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which gas is essential for breathing?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Oxygen"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which animal is known as the King of Jungle?",
        "options": ["Tiger", "Lion", "Elephant", "Bear"],
        "answer": "Lion"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["Salt", "Water", "Oxygen", "Hydrogen"],
        "answer": "Water"
    },
    {
        "question": "Which direction does the sun rise from?",
        "options": ["North", "South", "East", "West"],
        "answer": "East"
    },
    {
        "question": "How many letters are there in the English alphabet?",
        "options": ["24", "25", "26", "27"],
        "answer": "26"
    },

    # ---------- GUJARATI MCQs (10) ----------
    {
        "question": "ભારતની રાજધાની શું છે?",
        "options": ["દિલ્લી", "મુંબઈ", "ચેન્નઈ", "કોલકાતા"],
        "answer": "દિલ્લી"
    },
    {
        "question": "ગુજરાતની રાજધાની કઈ છે?",
        "options": ["સુરત", "રાજકોટ", "ગાંધીનગર", "અમદાવાદ"],
        "answer": "ગાંધીનગર"
    },
    {
        "question": "2 + 3 = ?",
        "options": ["4", "5", "6", "7"],
        "answer": "5"
    },
    {
        "question": "સૂર્ય કઈ દિશામાં ઉગે છે?",
        "options": ["ઉત્તર", "દક્ષિણ", "પૂર્વ", "પશ્ચિમ"],
        "answer": "પૂર્વ"
    },
    {
        "question": "ભારતના પ્રથમ વડાપ્રધાન કોણ હતા?",
        "options": ["ગાંધીજી", "જવાહરલાલ નેહરુ", "સરદાર પટેલ", "રાજેન્દ્ર પ્રસાદ"],
        "answer": "જવાહરલાલ નેહરુ"
    },
    {
        "question": "એક સપ્તાહમાં કેટલા દિવસ હોય છે?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "પાણીનું રાસાયણિક સૂત્ર શું છે?",
        "options": ["CO2", "H2O", "O2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "સિંહને કઈ રીતે ઓળખવામાં આવે છે?",
        "options": ["જંગલનો રાજા", "પાણીનો રાજા", "આકાશનો રાજા", "પર્વતનો રાજા"],
        "answer": "જંગલનો રાજા"
    },
    {
        "question": "માનવ શરીરમાં કેટલા ઇન્દ્રિયો છે?",
        "options": ["3", "4", "5", "6"],
        "answer": "5"
    },
    {
        "question": "ગુજરાત ભારતના કયા ભાગમાં આવેલું છે?",
        "options": ["ઉત્તર", "દક્ષિણ", "પૂર્વ", "પશ્ચિમ"],
        "answer": "પશ્ચિમ"
    }

]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, render_template
import os

app = Flask(__name__)

questions = [

    # ---------- ENGLISH MCQs (20) ----------
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

    {
        "question": "Who was the first President of India?",
        "options": ["Rajendra Prasad", "Jawaharlal Nehru", "Sardar Patel", "APJ Abdul Kalam"],
        "answer": "Rajendra Prasad"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Which continent is India located in?",
        "options": ["Europe", "Asia", "Africa", "Australia"],
        "answer": "Asia"
    },
    {
        "question": "Which month has 28 days in a normal year?",
        "options": ["January", "February", "March", "April"],
        "answer": "February"
    },
    {
        "question": "Which instrument is used to measure temperature?",
        "options": ["Barometer", "Thermometer", "Hygrometer", "Altimeter"],
        "answer": "Thermometer"
    },
    {
        "question": "Which bird cannot fly?",
        "options": ["Sparrow", "Eagle", "Ostrich", "Crow"],
        "answer": "Ostrich"
    },
    {
        "question": "Which is the national flower of India?",
        "options": ["Rose", "Lotus", "Lily", "Sunflower"],
        "answer": "Lotus"
    },
    {
        "question": "Which metal is liquid at room temperature?",
        "options": ["Iron", "Gold", "Mercury", "Silver"],
        "answer": "Mercury"
    },
    {
        "question": "Which day is celebrated as Independence Day in India?",
        "options": ["26 January", "15 August", "2 October", "1 May"],
        "answer": "15 August"
    },
    {
        "question": "How many colors are there in a rainbow?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },

    # ---------- GUJARATI MCQs (20) ----------
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
    },

    {
        "question": "ભારતનો રાષ્ટ્રધ્વજ કેટલા રંગનો છે?",
        "options": ["2", "3", "4", "5"],
        "answer": "3"
    },
    {
        "question": "ભારતનો રાષ્ટ્રીય પક્ષી કયું છે?",
        "options": ["કબૂતર", "મોર", "કાગડો", "ચકલી"],
        "answer": "મોર"
    },
    {
        "question": "ગુજરાતનું રાજ્ય ફૂલ કયું છે?",
        "options": ["ગુલાબ", "લોટસ", "મેરિગોલ્ડ", "સૂર્યમુખી"],
        "answer": "લોટસ"
    },
    {
        "question": "ગુજરાતનો સૌથી મોટો જિલ્લો કયો છે?",
        "options": ["કચ્છ", "અમદાવાદ", "સુરત", "વડોદરા"],
        "answer": "કચ્છ"
    },
    {
        "question": "ભારતની સ્વતંત્રતા ક્યારે મળી?",
        "options": ["1942", "1945", "1947", "1950"],
        "answer": "1947"
    },
    {
        "question": "વિશ્વ પર્યાવરણ દિવસ ક્યારે ઉજવાય છે?",
        "options": ["5 જૂન", "10 જુલાઈ", "15 ઓગસ્ટ", "2 ઑક્ટોબર"],
        "answer": "5 જૂન"
    },
    {
        "question": "ગુજરાતની રાજ્ય ભાષા કઈ છે?",
        "options": ["હિન્દી", "મરાઠી", "ગુજરાતી", "ઉર્દૂ"],
        "answer": "ગુજરાતી"
    },
    {
        "question": "ભારતનું રાષ્ટ્રીય ફળ કયું છે?",
        "options": ["કેળું", "સફરજન", "આમ", "નારંગી"],
        "answer": "આમ"
    },
    {
        "question": "વિશ્વનું સૌથી મોટું ખંડ કયું છે?",
        "options": ["યુરોપ", "આફ્રિકા", "એશિયા", "ઑસ્ટ્રેલિયા"],
        "answer": "એશિયા"
    },
    {
        "question": "ભારતની રાષ્ટ્રીય રમત કઈ છે?",
        "options": ["ક્રિકેટ", "ફૂટબોલ", "હોકી", "કબડ્ડી"],
        "answer": "હોકી"
    }

]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load FAQ dataset
with open("faq.json", "r") as f:
    faq_data = json.load(f)

def find_answer(question):
    for q, a in faq_data.items():
        if q.lower() in question.lower():
            return a
    return "Sorry, I don't know that yet."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"]
    answer = find_answer(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)

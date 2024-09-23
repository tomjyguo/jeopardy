import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

with open('questions.json') as f:
    QUESTIONS = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/question/<category>/<int:question_index>')
def show_question(category, question_index):
    question = QUESTIONS.get(category)[question_index]
    return render_template('question-page.html', category=category, question=question)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    correct_answer = QUESTIONS[data['category']][data['question_index']]['answer']
    is_correct = data['answer'].lower() == correct_answer.lower()
    return jsonify({"correct": is_correct, "correct_answer": correct_answer})

if __name__ == "__main__":
    app.run(debug=True)
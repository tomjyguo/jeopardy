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
    category_number = list(QUESTIONS.keys()).index(category) + 1
    question_number = question_index + 1
    return render_template('question-page.html', 
                           category=category, 
                           question=question, 
                           category_number=category_number, 
                           question_number=question_number)

@app.route('/mark_opened/<category>/<int:question_index>', methods=['POST'])
def mark_as_opened(category, question_index):
    QUESTIONS[category][question_index]['opened'] = True
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
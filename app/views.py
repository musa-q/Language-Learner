import csv
from flask import Blueprint, render_template, request
from components.verbs_manager import Verbs_Manager

views_blueprint = Blueprint('views', __name__)

verbsManager = Verbs_Manager()

def read_csv(file_path):
    flashcards = []
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=["arabic", "transliteration", "translation"])
            for row in reader:
                flashcards.append(row)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return flashcards

@views_blueprint.route('/')
def index():
    return render_template('index.html')

@views_blueprint.route('/verbs', methods=['GET', 'POST'])
def verbs():
    if request.method == 'POST':
        user_input = request.form.get('user-input')
        answer = verbsManager.get_answer()
        if user_input == answer:
            result = "Correct!"
        else:
            result = f"Incorrect. Answer is {answer}"
        return result
    else:
        (tense, pronoun, word) = verbsManager.get_random_conjugation()
        return render_template('verbs.html', tense=tense, pronoun=pronoun, word=word)


@views_blueprint.route('/words')
def words():
    file_title = "common_words.csv"
    filename = f"./app/components/arabic/{file_title}"
    flashcards = read_csv(filename)
    return render_template('words.html', flashcards=flashcards, filename=filename)

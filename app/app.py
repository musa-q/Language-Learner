import csv
from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
def index():
    file_title = "common_words.csv"
    filename = f"./app/arabic/{file_title}"
    flashcards = read_csv(filename)
    return render_template('index.html', flashcards=flashcards, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

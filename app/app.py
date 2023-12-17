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
    csv_file_path = "./app/arabic/words1.csv"
    flashcards = read_csv(csv_file_path)
    return render_template('index.html', flashcards=flashcards)

if __name__ == '__main__':
    app.run(debug=True)

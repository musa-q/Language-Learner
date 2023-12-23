import random
import os
import json


class Verbs_Manager:
    def __init__(self):
        self.file_path = os.path.join("app", "components", "arabic", "verbs")
        self.verb_data = {}
        self.tenses = ["present", "past", "future"]
        self.pronouns = ["i", "you_m", "you_f", "he", "she", "they", "we"]
        self.get_data()
        self.current_answer = None

    def get_data(self):
        for filename in os.listdir(self.file_path):
            f = os.path.join(self.file_path, filename)
            if os.path.isfile(f):
                file = open(f, "r", encoding='utf-8')
                data = json.load(file)
                self.verb_data[data["english"]] = data
                file.close()

    def get_random_conjugation(self):
        word_index = random.choice(list(self.verb_data.keys()))
        word = self.verb_data[word_index]
        tense = random.choice(self.tenses)
        pronoun = random.choice(self.pronouns)
        self.current_answer = word["conjugations"][tense][pronoun]
        return (tense, pronoun, word)

    def get_answer(self):
        return self.current_answer

    # def check_conjugation(self, answer, word, tense, pronoun):
    #     correct_answer = self.verb_data[word["english"]]["conjugations"][tense][pronoun]
    #     return answer.strip() == correct_answer.strip()
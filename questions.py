import json
import random

def load_questions():
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    random.shuffle(questions)
    return questions
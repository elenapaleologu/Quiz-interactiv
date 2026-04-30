import requests
import random

def load_questions():

    url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

    try:
        response = requests.get(url, timeout=5)
        data = response.json().get("results", [])

        if not data:
            return []

        questions = []

        for item in data:

            question = item["question"]
            correct = item["correct_answer"]
            wrong = item["incorrect_answers"]

            options = wrong + [correct]
            random.shuffle(options)

            letters = ["A", "B", "C", "D"]
            correct_letter = letters[options.index(correct)]

            questions.append({
                "question": question,
                "options": [f"{letters[i]}. {options[i]}" for i in range(4)],
                "answer": correct_letter
            })

        return questions

    except:
        return []
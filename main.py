from questions import load_questions
from scores import save_score, show_scores
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Răspunsul tău (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("✔ Corect!")
        return True
    else:
        print(f"✘ Greșit! Răspunsul corect era {q['answer']}")
        return False

def start_quiz():
    clear_screen()
    print("=== START QUIZ ===")

    name = input("Introdu numele tău: ")
    score = 0

    questions = load_questions()

    for q in questions:
        if ask_question(q):
            score += 1

    print(f"\n🎉 {name}, ai obținut {score}/{len(questions)} puncte!")
    save_score(name, score)

    input("\nApasă Enter pentru a reveni...")
    clear_screen()

def main_menu():
    while True:
        print("\n=== QUIZ MASTER ===")
        print("1. Start Quiz")
        print("2. Vezi scoruri")
        print("3. Ieșire")

        choice = input("Alege o opțiune: ")

        if choice == "1":
            start_quiz()
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă!")

if __name__ == "__main__":
    main_menu()
import json
import os

SCORES_FILE = "scores.json"

def save_score(name, score):
    data = []

    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = []

    data.append({"name": name, "score": score})

    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def show_scores():
    print("\n=== SCORURI ===")

    if not os.path.exists(SCORES_FILE):
        print("Nu există scoruri încă.")
        input("\nApasă Enter...")
        return

    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.sort(key=lambda x: x["score"], reverse=True)

    for i, entry in enumerate(data[:10], start=1):
        print(f"{i}. {entry['name']} - {entry['score']} puncte")

    input("\nApasă Enter pentru a reveni...")
import json
import os

FILE_SCORE = "scores.json"

def load_scores():
    if not os.path.exists(FILE_SCORE):
        return []

    try:
        with open(FILE_SCORE, "r") as file:
            return json.load(file)
    except:
        return []

def save_score(name, score):
    scores = load_scores()
    scores.append({
        "name": name,
        "score": score
    })

    scores.sort(key=lambda x: x["score"], reverse=True)

    with open(FILE_SCORE, "w") as file:
        json.dump(scores, file, indent=4)

def show_top5():
    scores = load_scores()

    if not scores:
        print("\nBelum ada skor.")
        return

    print("\n=== TOP 5 SCORE ===")
    for i, data in enumerate(scores[:5], start=1):
        print(f"{i}. {data['name']} - {data['score']} pts")
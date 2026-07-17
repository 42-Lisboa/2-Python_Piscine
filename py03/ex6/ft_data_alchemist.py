#! /usr/bin/env python3

import random


PLAYERS = ['Alice', 'bob', 'Charlie', 'dylan', 'Alex',
           'Emma', 'Gregory', 'john', 'kevin', 'Liam']


# ====================== Inventory Function Creation =========================

def data_alchemist() -> None:
    print("\n================ 📅  Game Data Alchemist 📅  =================\n")
    print(f"➡️  Initial list of players: {PLAYERS}\n")

    # >>>>> 1st Comprehension (List):
    apply_capitalize = [name.capitalize() for name in PLAYERS]
    print(f"✅ New list with all names capitalized: {apply_capitalize}\n")

    # >>>>> 2nd Comprehension (List):
    origin_capitalize = [name for name in PLAYERS if name == name.capitalize()]
    print(f"✅ New list with names originally capitalized: {origin_capitalize}")

    # >>>>> 3rd Comprehension (Dict):
    score_dict = {name: random.randint(50, 1000) for name in apply_capitalize}
    print(f"\n📊 Score dict: {score_dict}\n")

    scores = score_dict.values()
    average = sum(scores) / len(scores)
    print(f"📏 Score average is {(average):.2f}\n")

    # >>>>> 4th Comprehension (Dict):
    high_scores = {p: s for p, s in score_dict.items() if s > average}
    print(f"🏆 High scores: {high_scores}\n")


# ============================== Program Test ================================

if __name__ == "__main__":
    data_alchemist()

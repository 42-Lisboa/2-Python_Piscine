#! /usr/bin/env python3

import random


# ======================= Achievements Set Creation ==========================

def gen_player_achievements() -> set:
    achievements_list = [
         "🛠️  Crafting Genius",
         "🌍  World Savior",
         "🗺️  Master Explorer",
         "💎  Collector Supreme",
         "🛡️  Untouchable",
         "⚔️  Boss Slayer",
         "⚒️  Forge Master",
         "🕊️  Realm Liberator",
         "🧭  Uncharted Pathfinder",
         "🏺  Relic Hunter",
         "🥷  Flawless Assassin",
         "🐉  Dragon Bane",
         "🧪  Alchemy Prodigy",
         "🦸  Champion of Light",
         "🏔️  Summit Conqueror",
         "💰  Treasure Hoarder",
         "👻  Phantom Dodger",
         "👹  Monster Crusher",
         "⚙️  Gadget Inventor",
         "👑  Ultimate Legend"
    ]
    number_set = random.randint(1, 10)
    achievements_set = set(random.sample(achievements_list, k=number_set))
    return achievements_set


# ====================== Achievements Tracker System =========================

def achievements_tracker_system() -> None:
    print("\n============= ⚔️  Achievements Tracker System ⚔️ =============\n")

    players: dict = {
        "Alice": set(),
        "Bob": set(),
        "Charlie": set(),
        "Dylan": set()
        }

    for player in players:
        players[player] = gen_player_achievements()
        print(f"🎮 Player {player}: {players[player]}")

    achievements_union = (players["Alice"] |
                          players["Bob"] |
                          players["Charlie"] |
                          players["Dylan"])
    print(f"\n✅ All distinct achievements: {achievements_union}")


# ============================== Program Test ================================

if __name__ == "__main__":
    achievements_tracker_system()

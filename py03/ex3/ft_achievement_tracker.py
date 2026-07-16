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
    number_set = random.randint(4, 20)
    achievements_set = set(random.sample(achievements_list, k=number_set))
    return achievements_set


# ====================== Achievements Tracker System =========================

def achievements_tracker_system() -> None:
    print("\n============= ⚔️  Achievements Tracker System ⚔️  ============\n")
    # ----------------------------------------- Creating the achievements dict
    players: dict = {
        "Alice": set(),
        "Bob": set(),
        "Charlie": set(),
        "Dylan": set()
        }
    for player in players:
        players[player] = gen_player_achievements()
        print(f"🎮 Player {player}: {players[player]}")
        print("------------------------------------------------------------")

    # ---------------------------------------------------- (Union | .union())
    achievements_union = (players["Alice"] |
                          players["Bob"] |
                          players["Charlie"] |
                          players["Dylan"])
    # achievements_union = set.union(*players.values()) - another way to unite
    print("\nUnlocked achievements (Union)\n"
          "------------------------------\n"
          f"{achievements_union}\n")

    # -------------------------------------- (Intersection & .intersection())
    achievements_inter = set.intersection(*players.values())
    print("Shared achievements (Intersection)\n"
          "-----------------------------------\n"
          f"{achievements_inter}\n")

    # ------------------------------------------ (Difference - .difference())
    print("Exclusive achievements (Difference)\n"
          "------------------------------------")
    for player, player_set in players.items():
        # 🔰 On this line we use comprehension list - for and if in one line
        rivals_sets = [s for rival, s in players.items() if rival != player]

        # 🔰 Could be also written like this:
        # rivals_sets = []
        # for rival, s in players.items():
        #    if rival != player:
        #        rivals_sets.append(s)

        achievements_diff1 = player_set.difference(*rivals_sets)
        print(f"Only {player} has: {achievements_diff1}")

    # ------------------------------------------ (Difference - .difference())
    print("\nMissing achievements (Difference)\n"
          "----------------------------------")
    achievements_list = set([
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
    ])
    for player, player_set in players.items():
        achievements_diff2 = achievements_list.difference(player_set)
        print(f"{player} is missing: {achievements_diff2}\n"
              f">>>>>>>>>>>>>>>> Total missing: {len(achievements_diff2)}\n"
              "----------------------------------")


# ============================== Program Test ================================

if __name__ == "__main__":
    achievements_tracker_system()

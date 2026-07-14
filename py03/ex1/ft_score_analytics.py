#! /usr/bin/env python3

import sys


# ======================= Score Analytics Creation ==========================

def ft_score_analytics(argv: list) -> None:
    total_argv = len(argv)

    print("\n================= 🎮  Player Score Analytics 🎮 =================")
    if total_argv == 1:
        print(" ⭕ No scores provided. "
              "Usage: ./ft_score_analytics.py <score1> <score2> ...")
        return

    players = []
    for arg in argv[1:]:
        try:
            arg_int = int(arg)
            players.append(arg_int)
        except ValueError:
            print(f"❌ Invalid parameter: '{arg}'")
            pass

    print(f"👾 Scores processed:   {players}")
    print(f"👾 Total players:      {len(players)}")
    print(f"👾 Total score:        {sum(players)}")
    print(f"👾 Average score:      {(sum(players) / len(players)):.2f}")
    print(f"👾 High score:         {max(players)}")
    print(f"👾 Low score:          {min(players)}")
    print(f"👾 Score range:        {max(players) - min(players)}\n")


# ============================== Program Test ================================

if __name__ == "__main__":
    argv = sys.argv
    ft_score_analytics(argv)

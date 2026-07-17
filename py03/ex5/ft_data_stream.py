#! /usr/bin/env python3

import typing
import random

PLAYERS_LIST = [
    "Alice",
    "Bob",
    "Charlie",
    "Dylan",
    "Edgard",
    "Fabio"
]

ACTIONS_LIST = [
    "run 🏃",
    "sleep 💤",
    "eat 🍽️",
    "move 🚶",
    "climb 🧗",
    "swim 🏊",
    "jump 🦘",
    "fly 🦅"
]


# ====================== Generators Functions Creation ========================

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    # YieldType = tuple[str, str]
    # SendType = None
    # ReturnType = None
    while True:
        new_player = random.choice(PLAYERS_LIST)
        new_action = random.choice(ACTIONS_LIST)
        yield (new_player, new_action)


def consume_event(events_list: list) -> typing.Generator[tuple[str, str],
                                                         None, None]:
    while events_list:
        event = random.choice(events_list)
        events_list.remove(event)
        yield event


# ====================== Stream Data Processor Function =======================

def game_data_stream() -> None:
    print("\n============= ⚔️  Game Data Stream Processor ⚔️  =============\n")
    event_gen = gen_event()

    for i in range(1000):
        event = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events_list = [next(event_gen) for i in range(10)]  # comprehension list
    print(f"\nBuilt list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"\nGot event from list: {event}")
        print(f"Remains in list: {events_list}")
        print(f">>>>>>> Remains: {len(events_list)}")


# ============================== Program Test ================================

if __name__ == "__main__":
    game_data_stream()

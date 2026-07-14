#! /usr/bin/env python3

import math


# ======================= Score Analytics Creation ==========================

def get_player_pos() -> tuple:
    while True:
        string_input = input("Enter new coordinates as "
                             "floats in format 'x,y,z': ")

        string_splitted = string_input.split(',')
        if len(string_splitted) != 3:
            print("⭕ Invalid syntax")
            continue

        coordinates_list = []
        for str in string_splitted:
            try:
                coordinates_list.append(float(str))
            except ValueError as e:
                print(f"❌ Error on parameter '{str}': {e}")
                continue
        if len(coordinates_list) == 3:
            coordinates_tuple = tuple(coordinates_list)
            break
    return coordinates_tuple


def game_coordinate_system() -> None:
    print("\n================= 🎮  Game Coordinate System 🎮 =================")

    print("\n📍 === Get a first set of coordinates === 📍")
    coords1 = get_player_pos()
    print(f"Got a first tuple: {coords1}")
    print(f"It includes: X = {coords1[0]}, Y = {coords1[1]}, Z = {coords1[2]}")
    distance2center = math.sqrt(  # Euclidean Distance Formula
        (coords1[0]-0)**2 +
        (coords1[1]-0)**2 +
        (coords1[2]-0)**2)
    print(f"✅ Distance to center: {(distance2center):.4f}")

    print("\n📍 === Get a second set of coordinates === 📍")
    coords2 = get_player_pos()
    print(f"Got a second tuple: {coords2}")
    print(f"It includes: X = {coords2[0]}, Y = {coords2[1]}, Z = {coords2[2]}")
    distance2points = math.sqrt(   # Euclidean Distance Formula
        (coords2[0]-coords1[0])**2 +
        (coords2[1]-coords1[1])**2 +
        (coords2[2]-coords1[2])**2)
    print(f"✅ Distance between two coordinates: {(distance2points):.4f}\n")


# ============================== Program Test ================================

if __name__ == "__main__":
    game_coordinate_system()

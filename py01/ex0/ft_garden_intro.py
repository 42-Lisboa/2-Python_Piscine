#! /usr/bin/env python3

def garden_intro() -> None:
    plant = input("Plant: ")
    height = 0
    while height <= 0:
        height = int(input("Height: "))
    age = 0
    while age <= 0:
        age = int(input("Age: "))

    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    if age == 1:
        print(f"Age: {age} day")
    else:
        print(f"Age: {age} days")
    print("====== End of Program ======")


if __name__ == "__main__":
    garden_intro()

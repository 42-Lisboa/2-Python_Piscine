#! usr/bin/env python3

class Plant:
    def __init__(self):
        plant = input("Plant: ")
        height = 0
        while height <= 0:
            height = int(input("Height: "))
        age = 0
        while age <= 0:
            age = int(input("Age: "))

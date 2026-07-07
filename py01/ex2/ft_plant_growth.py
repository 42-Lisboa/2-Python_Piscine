#! /usr/bin/env python3

class Plant:
    def __init__(
            self,
            plant_name: str, height: float,
            current_age: int, growth_rate: float, days: int):
        self.plant_name = plant_name
        self.height = height
        self.current_age = current_age
        self.growth_rate = growth_rate
        self.days = days

    def grow(self) -> None:
        self.height = (self.growth_rate / 100) * self.height

    def age(self) -> None:
        self.current_age += 1

    def show(self) -> None:
        print(
            f"{self.plant_name.capitalize()}: "
            f"{self.height}cm, {self.age} days old")
        for i in range(1, self.days + 1):
            self.grow()
            self.age()
            print(
                f"{self.plant_name.capitalize()}: "
                f"{self.height}cm, {self.age} days old")


def plant_growth() -> None:
    plant1 = Plant(
        input("Plant: "), int(input("Height: ")), int(input("Age: ")),
        int(input("Growth rate (%): ")), int(input("Growth days: ")))
    
    print("=== Garden Plant Growth ===")



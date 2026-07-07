#! /usr/bin/env python3

class Plant:
    def __init__(self, plant_name: str, height: int, age: int):
        self.plant_name = plant_name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(
            f"{self.plant_name.capitalize()}: "
            f"{self.height}cm, {self.age} days old")


def garden_data() -> None:
    plant1 = Plant(input("1st Plant: "),
                   int(input("Height: ")), int(input("Age: ")))
    plant2 = Plant(input("2nd Plant: "),
                   int(input("Height: ")), int(input("Age: ")))
    plant3 = Plant(input("3rd Plant: "),
                   int(input("Height: ")), int(input("Age: ")))

    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()


if __name__ == "__main__":
    garden_data()

#! /usr/bin/env python3

# ========== Plant Class with Growth and Age Methods ==========

class Plant:
    def __init__(
            self,
            plant_name: str, height: float,
            current_age: int, growth_cm: float = 2.0, days: int = 7):
        self.plant_name = plant_name
        self.height = height
        self.current_age = current_age
        self.growth_cm = growth_cm
        self.days = days

    def grow(self) -> None:
        self.height += self.growth_cm

    def age(self) -> None:
        self.current_age += 1

    def apply_growth(self, days: int = 1) -> None:
        for _ in range(days):
            self.grow()
            self.age()

    def show(self) -> None:
        print(
            f"{self.plant_name.capitalize()}: "
            f"{self.height:.1f}cm, {self.current_age} days old")


# ======================= Plant Factory =======================

def plant_factory() -> None:
    garden_plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    print("======= Plant Factory Output =======")
    for plant in garden_plants:
        print("Created: ", end="")
        plant.show()


# ======================= Program Test ========================

if __name__ == "__main__":
    plant_factory()

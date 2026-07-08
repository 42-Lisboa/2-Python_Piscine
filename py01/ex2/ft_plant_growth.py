#! /usr/bin/env python3

# ========== Plant Class with Growth and Age Methods ==========

class Plant:
    def __init__(
            self,
            plant_name: str, height: float,
            current_age: int, growth_cm: float, days: int):
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


# =================== Plant Growth Simulator ===================

def plant_growth_simulator() -> None:
    plant1 = Plant(
        input("Plant: "), float(input("Height: ")), int(input("Age: ")),
        float(input("Growth (cm/day): ")), int(input("Growth days: ")))

    initial_height = plant1.height
    print("=== Garden Plant Growth ===")
    plant1.show()
    for i in range(1, plant1.days + 1):
        plant1.apply_growth()
        print(f"=== Day {i} ===")
        plant1.show()

    total_growth = plant1.height - initial_height
    print(f"Growth this week: {total_growth:.1f}cm")


# ======================= Program Test ========================

if __name__ == "__main__":
    plant_growth_simulator()

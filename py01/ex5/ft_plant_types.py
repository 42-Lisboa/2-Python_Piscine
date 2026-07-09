#! /usr/bin/env python3

# ======== Encapsulated Plant Class with Growth and Age Methods  ========

class Plant:
    def __init__(
            self,
            plant_name: str, height: float,
            current_age: int, growth_cm: float = 2.0, days: int = 7):
        self._plant_name = plant_name
        self._height = height
        self._current_age = current_age
        self.growth_cm = growth_cm
        self.days = days

    def grow(self) -> None:
        self._height += self.growth_cm

    def age(self) -> None:
        self._current_age += 1

    def apply_growth(self, days: int = 1) -> None:
        for _ in range(days):
            self.grow()
            self.age()

    def show(self) -> None:
        print(
            f"{self._plant_name.capitalize()}: "
            f"{self._height:.1f}cm, {self._current_age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._current_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"\n{self._plant_name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"\n{self._plant_name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._current_age = new_age


# ======================== Inheritted Plant Classes  ========================

class Flower(Plant):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, color: str, is_bloomed: bool = False):

        super().__init__(plant_name, height, current_age)

        self.color = color
        self.is_bloomed = is_bloomed

    def bloom(self) -> None:
        if not self.is_bloomed:
            self.is_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloomed:
            print(f" {self._plant_name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._plant_name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, trunk_diameter: float):

        super().__init__(plant_name, height, current_age)

        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._plant_name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, harvest_season: str,
                 nutritional_value: int = 0):

        super().__init__(plant_name, height, current_age)

        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest Season: {self.harvest_season.capitalize()}")
        print(f" Nutritional Value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1


# ======================== Garden Plant Types function ========================

def plant_types() -> None:

    print("\n================== 🌽 Garden Plant Types 🌽 ==================\n")

    print("\n=============== 🌹 Flower\n")
    flower1 = Flower("rose", 15.0, 10, "red")
    flower1.show()
    print(f"[asking the {flower1._plant_name.capitalize()} to bloom] 🔄")
    flower1.bloom()
    flower1.show()

    print("\n=============== 🌳 Tree\n")
    tree1 = Tree("oaK", 200.0, 365, 5.0)
    tree1.show()
    print(f"[asking the {tree1._plant_name.capitalize()} "
          f"to produce shade] 🔄")
    tree1.produce_shade()

    print("\n=============== 🥕 Vegetable\n")
    vegetable1 = Vegetable("Tomato", 5.0, 10, "april")
    vegetable1.show()
    g_days = 20
    print(f"[make {vegetable1._plant_name.capitalize()} "
          f"grow and age for {g_days} days] 🔄")
    vegetable1.apply_growth(g_days)
    vegetable1.show()


# ============================ Program Test =============================

if __name__ == "__main__":
    plant_types()

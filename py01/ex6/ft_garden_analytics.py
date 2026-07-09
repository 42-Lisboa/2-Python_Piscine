#! /usr/bin/env python3

# === Encapsulated Plant Class with Growth, Age, Static and Class Methods  ===

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
        self._stats_grow = 0
        self._stats_age = 0
        self._stats_show = 0

    def grow(self) -> None:
        self._height += self.growth_cm
        self._stats_grow += 1

    def age(self) -> None:
        self._current_age += 1
        self._stats_age += 1

    def apply_growth(self, days: int = 1) -> None:
        for _ in range(days):
            self.grow()
            self.age()

    def show(self) -> None:
        print(
            f"{self._plant_name.capitalize()}: "
            f"{self._height:.1f}cm, {self._current_age} days old")
        self._stats_show += 1

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

    def get_stats(self) -> dict:
        return {
            "name": self._plant_name,
            "grow": self._stats_grow,
            "age": self._stats_age,
            "show": self._stats_show
        }

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls,
                         plant_name: str = "Unknown plant",
                         height: float = 0.0, current_age: int = 0,
                         growth_cm: float = 0.0
                         ) -> 'Plant':
        return cls(plant_name, height, current_age, growth_cm)


# ======================== Inheritted Plant Classes  =========================

class Flower(Plant):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, color: str, is_bloomed: bool = False):

        super().__init__(plant_name, height, current_age)
        self.color = color
        self.is_bloomed = is_bloomed
        self._stats_bloom = 0

    def bloom(self) -> None:
        if not self.is_bloomed:
            self.is_bloomed = True
        self._stats_bloom += 1

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloomed:
            print(f" {self._plant_name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._plant_name.capitalize()} has not bloomed yet")

    def get_stats(self) -> dict:
        stats = super().get_stats()
        stats["bloom"] = self._stats_bloom
        return stats


class Seed(Flower):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, color: str, seeds: int = 0):

        super().__init__(plant_name, height, current_age, color)
        self.seeds = seeds

    def grow(self) -> None:
        super().grow()
        self.seeds += 1

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, plant_name: str, height: float,
                 current_age: int, trunk_diameter: float):

        super().__init__(plant_name, height, current_age)
        self.trunk_diameter = trunk_diameter
        self._stats_shade = 0

    def produce_shade(self) -> None:
        print(
            f"Tree {self._plant_name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self._stats_shade += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk Diameter: {self.trunk_diameter}cm")

    def get_stats(self) -> dict:
        stats = super().get_stats()
        stats["shade"] = self._stats_shade
        return stats


# ======================  Show Statistics function  ======================

def show_stats(plant: Plant) -> None:
    stats_dict = plant.get_stats()
    print(f"[statistics for {stats_dict['name'].capitalize()}]")
    print(f"Stats: "
          f"{stats_dict['grow']} grow, "
          f"{stats_dict['age']} age, "
          f"{stats_dict['show']} show"
          )
    if 'bloom' in stats_dict:
        print(f" {stats_dict['bloom']} bloom")
    if 'shade' in stats_dict:
        print(f" {stats_dict['shade']} shade")


# ====================== Garden Analytics function ======================

def garden_analytics() -> None:

    print("\n================== 📊 Garden Statistics 📊 ==================\n")

    print("\n=============== 📅 Check year-old\n")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=============== 🌹 Flower\n")
    flower1 = Flower("Rose", 15.0, 10, "red")
    flower1.show()
    show_stats(flower1)
    print(f"[asking the {flower1._plant_name.lower()} "
          f"to grow, age and bloom] 🔄")
    # From 15cm to 23cm (2.0cm growth / day)
    flower1.apply_growth(4)
    flower1.bloom()
    flower1.show()
    show_stats(flower1)

    print("\n=============== 🌳 Tree\n")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    tree1.show()
    show_stats(tree1)
    print(f"[asking the {tree1._plant_name.lower()} to produce shade] 🔄")
    tree1.produce_shade()
    show_stats(tree1)

    print("\n=============== 🌱 Seed\n")
    seed1 = Seed("Sunflower", 80.0, 45, "yellow")
    seed1.show()
    print(f"[make {seed1._plant_name.lower()} grow, age and bloom] 🔄")
    seed1.apply_growth(20)
    seed1.bloom()
    seed1.show()
    show_stats(seed1)

    print("\n=============== 👻 Anonymous\n")
    anon1 = Plant.create_anonymous()
    anon1.show()
    show_stats(anon1)


# ============================ Program Test =============================

if __name__ == "__main__":
    garden_analytics()

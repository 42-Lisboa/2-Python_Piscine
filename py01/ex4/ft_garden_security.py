#! /usr/bin/env python3

# ====== Encapsulated Plant Class with Growth and Age Methods  ======

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


# ===================== Garden Security function =====================

def garden_security_system() -> None:
    print("\n=== Garden Security System ===")

    # 1. Instatiate the object
    plant1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant1.show()

    # 2. Test set and get methods with valid inputs
    print("\n✨ Now let's update height and age with valid inputs! ✨")
    valid_height = float(input("Enter new valid height: "))
    plant1.set_height(valid_height)
    valid_age = int(input("Enter new valid age: "))
    plant1.set_age(valid_age)
    print(f"Height updated: {plant1.get_height()}cm")
    print(f"Age updated: {plant1.get_age()} days\n")

    # 4. Test set method with invalid inputs
    print("🙅 Now let's update height and age with invalid inputs! 🙅")
    invalid_height = float(input("Enter negative height: "))
    invalid_age = int(input("Enter negative age: "))
    plant1.set_height(invalid_height)
    plant1.set_age(invalid_age)

    # 5. Proof that the security worked
    print("\nCurrent state: ", end="")
    plant1.show()


# ============================ Program Test =============================

if __name__ == "__main__":
    garden_security_system()

#! /usr/bin/env python3

# =========================== New Errors Creation ============================

class GardenError(Exception):  # For problems with garden
    def __init__(self, message="❌ Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):  # For problems with plants
    pass


class WaterError(GardenError):  # For problems with watering
    pass


# ======================= Specific Scenario functions =========================

def garden_plant_newseed(has_space: bool = False) -> None:  # Garden Function 💐
    if has_space:
        print("🌱 Seed was planted on the garden!")
    else:
        raise GardenError("Seed wasn't planted - lack enough garden area")


def harvest_plant(age_str: str) -> None:  # >>>>>>>>>>>>>>>>> Plant Function 🌱
    age = int(age_str)
    if age >= 50:
        print("🍇 Plant was harvested!")
    else:
        raise PlantError("Plant wasn't ready to be harvested!")


def water_plants(tank_water_level: float) -> None:  # >>>>>>> Water Function 💧
    if tank_water_level >= 2.5:
        print("💧 Plants were watered!")
    else:
        raise WaterError("Not enough water in the tank for the plants!")


# ============================ Custom Errors Demo =============================

def custom_errors_demo() -> None:
    print("================ 💭 Custom Garden Errors Demo 💭 ===============\n")

    print("Testing GardenError...")

    try:
        garden_plant_newseed()
    except GardenError as e:
        print(f"❌ Caught GardenError: {e}")
    print(">>> New good test! <<<")
    garden_plant_newseed(True)

    print("\nTesting PlantError...")

    try:
        harvest_plant("42")
    except PlantError as e:
        print(f"❌ Caught PlantError: {e}")
    print(">>> New good test! <<<")
    harvest_plant("55")

    print("\nTesting WaterError...")

    try:
        water_plants(2.1)
    except WaterError as e:
        print(f"❌ Caught WaterError: {e}")
    print(">>> New good test! <<<")
    water_plants(2.9)

    print("\nTesting catching all garden errors...")

    errors_to_simulate = [
        GardenError("Seed wasn't planted - lack enough garden area"),
        PlantError("Plant wasn't ready to be harvested!"),
        WaterError("Not enough water in the tank for the plants!")
    ]
    for error in errors_to_simulate:
        try:
            raise error
        except GardenError as e:
            print(f"❌ Caught GardenError: {e}")

    print("\n⭐ All custom error types work correctly! ⭐")


# ============================== Program Test ================================

if __name__ == "__main__":
    custom_errors_demo()

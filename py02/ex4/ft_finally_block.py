#! /usr/bin/env python3

# =========================== New Errors Creation ============================

class GardenError(Exception):  # For problems with garden
    def __init__(self, message="❌ Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):  # For problems with plants
    pass


# =========================== Water Plant function ============================

def water_plant(plant_name: str) -> None:
    plant_name_capitalized = plant_name.capitalize()
    if plant_name == plant_name_capitalized:
        print(f"💧 Watering {plant_name_capitalized}: [OK]")
    else:
        raise PlantError(f"❌ Caught PlantError: "
                         f"Invalid plant name to water: '{plant_name}'")


# ======================== Water System Test function =========================

def test_watering_system() -> None:
    print("================ 🌻 Garden Watering System 🌻 ===============\n")

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"{e}\n... ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"{e}\n... ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print("✅ Cleanup always happens, even with errors!")


# ============================== Program Test ================================

if __name__ == "__main__":
    test_watering_system()

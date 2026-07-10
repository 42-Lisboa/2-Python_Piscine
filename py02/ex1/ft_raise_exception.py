#! /usr/bin/env python3

# ============================ Input Temperature =============================

def input_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C) ❄️")
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C) 🔥")
        return temp

    except ValueError as e:
        print(f"❌ Error: {e}")
        return None

    except Exception as e:
        print(f"❌ Error: Something went wrong with the sensor! Details: {e}")
        return None


# ===================== Temperature Testing function ======================

def test_temperature() -> None:
    print("=============== 🌡️  Garden Temperature🌡️  ===============")

    input_data = "25"
    output_data = input_temperature(input_data)
    print(f"\nInput data is '{input_data}'")
    print(f"⛅ Temperature is now {output_data}°C")

    input_data = "abc"
    print(f"\nInput data is '{input_data}'")
    input_temperature(input_data)

    input_data = "100"
    print(f"\nInput data is '{input_data}'")
    input_temperature(input_data)

    input_data = "-50"
    print(f"\nInput data is '{input_data}'")
    input_temperature(input_data)

    input_data_list = [24, 32]
    print(f"\nInput data is '{input_data_list}'")
    input_temperature(input_data_list)  # type: ignore

    print("\n✅ All tests completed - program didn't crash!")


# ============================= Program Test ==============================

if __name__ == "__main__":
    test_temperature()

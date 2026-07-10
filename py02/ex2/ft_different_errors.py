#! /usr/bin/env python3

# ========================= Error Operations function =========================

def garden_operation(op_number: int) -> None:
    if op_number == 0:
        int("abc")
    elif op_number == 1:
        _ = 42 / 0  # type: ignore
    elif op_number == 2:
        open("file_not_found.txt")
    elif op_number == 3:
        _ = 40 + "dois"  # type: ignore
    else:
        return


# ========================= Test Error Types function =========================

def test_error_types() -> None:
    print("================= 🌽 Garden Error Types Demo 🌽 =================\n")

    for i in "01234":  # Instead range(5), used a random string(size = 5)
        print(f"Testing operation {i}...")

        try:
            garden_operation(int(i))
            print("✅ Operation completed successfully")
        except ValueError as e:
            print(f"❌ Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"❌ Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"❌ Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"❌ Caught TypeError: {e}")

    print("\n⭐ All error types tested successfully! ⭐")


# ============================== Program Test ================================

if __name__ == "__main__":
    test_error_types()

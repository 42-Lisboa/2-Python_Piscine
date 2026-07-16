#! /usr/bin/env python3

import sys


# ====================== Inventory Function Creation =========================

def fill_inventory(items_input: list) -> dict:
    if len(items_input) == 0:
        print("⭕ Invalid syntax. Usage: [./ft_inventory_system.py "
              "<item_name>:<quantity> <item_name>:<quantity>]")
        sys.exit()

    inventory: dict = {}
    for item in items_input:
        temp = item.split(':')

        if len(temp) != 2:
            print(f"❌ Error - invalid parameter {temp}")
            continue
        if temp[0] in inventory:
            print(f"❌ Redundant item '{temp[0]}' - discarding")
            continue
        try:
            inventory[temp[0]] = int(temp[1])
        except ValueError as e:
            print(f"❌ Quantity error for '{temp[0]}': {e}")

    return inventory


# ====================== Inventory System Function =========================

def inventory_system_analysis(items_input: list) -> None:
    inventory = fill_inventory(items_input)

    print("\n============= ⚔️  Inventory System Analysis ⚔️  ============\n")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")


# ============================== Program Test ================================

if __name__ == "__main__":
    inventory_system_analysis(sys.argv[1:])

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
            print(f"❌ Error - invalid parameter '{item}'")
            continue
        if temp[0] in inventory:
            print(f"❌ Redundant item '{temp[0]}' - discarding")
            continue
        try:
            inventory[temp[0]] = int(temp[1])
        except ValueError as e:
            print(f"❌ Quantity error for '{temp[0]}': {e}")

    return inventory


# ========================= Inventory System Function =========================

def inventory_system_analysis(items_input: list) -> None:
    inv = fill_inventory(items_input)

    print("\n============== ⚔️  Inventory System Analysis ⚔️  =============\n")
    print(f"✅ Got inventory: {inv}")
    print(f"📜 Item list: {list(inv.keys())}")

    total_qty = sum(inv.values())
    print(f"🧮 Total quantity of the {len(inv)} items: {total_qty}")

    for item, quantity in inv.items():
        item_weight = (quantity / total_qty) * 100
        print(f"  📊 Item {item} represents\t{(item_weight):.1f}%")

    max_val = max(inv.values())
    max_key = ""
    for item, quantity in inv.items():
        if quantity == max_val:
            max_key = item
            break
    min_val = min(inv.values())
    min_key = ""
    for item, quantity in inv.items():
        if quantity == min_val:
            min_key = item
            break
    # Another way to use the max and min with the key and get function
    # max_item = max(inv, key=inv.get)  # type: ignore
    # min_item = min(inv, key=inv.get)  # type: ignore
    print(f"⬆️  Item most abundant: {max_key} with quantity {max_val}")
    print(f"⬇️  Item least abundant: {min_key} with quantity {min_val}")

    inv["magic_item"] = 1
    print(f"✨ Updated inventory: {inv}\n")


# ============================== Program Test ================================

if __name__ == "__main__":
    inventory_system_analysis(sys.argv[1:])

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    unit_formats = {
        "packets": f"{quantity} packets available",
        "grams": f"{quantity} grams total",
        "area": f"covers {quantity} square meters"
    }
    if unit not in unit_formats:
        print("Unknown unit type")
        return
    else:
        print(f"{seed_type.capitalize()} seeds: {unit_formats[unit]}")

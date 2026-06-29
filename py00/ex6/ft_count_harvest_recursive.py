def ft_recursive_print(days: int, current_day: int = 1) -> None:
    if current_day > days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_recursive_print(days, current_day + 1)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    ft_recursive_print(days)

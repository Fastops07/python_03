import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or not parts[0].strip():
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = parts[0].strip()
        quantity_str: str = parts[1].strip()
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity: int = int(quantity_str)
        except ValueError as err:
            print(f"Quantity error for '{item}': {err}")
            continue

        inventory[item] = quantity
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    print(f"Item list: {list(inventory.keys())}")

    total_quantity: int = sum(inventory.values())

    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if total_quantity == 0:
        print("Cannot compute percentages: total quantity is 0")
    else:
        for item in inventory.keys():
            percentage: float = round(
                inventory[item] / total_quantity * 100, 1
            )
            print(f"Item {item} represents {percentage}%")

    most_abundant_item: str = ""
    highest_quantity: int = 0
    least_abundant_item: str = ""
    lowest_quantity: int = 0
    first_item: bool = True

    for item in inventory.keys():
        curr_value: int = inventory[item]
        if first_item:
            most_abundant_item = item
            highest_quantity = curr_value
            least_abundant_item = item
            lowest_quantity = curr_value
            first_item = False
        else:
            if curr_value > highest_quantity:
                most_abundant_item = item
                highest_quantity = curr_value

            if curr_value < lowest_quantity:
                least_abundant_item = item
                lowest_quantity = curr_value

    print(
        f"Item most abundant: {most_abundant_item} "
        f"with quantity {highest_quantity}"
    )
    print(
        f"Item least abundant: {least_abundant_item} "
        f"with quantity {lowest_quantity}"
    )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:

        splited_args: list[str] = arg.split(":")
        if len(splited_args) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = splited_args[0]
        quantity_str: str = splited_args[1]
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

    print(list(inventory.keys()))

    print(
        f"Total quantity of the {len(inventory)} "
        f"items: {sum(inventory.values())}"
    )

    for key, value in inventory.items():
        print(
            f"Item {key} represents "
            f"{round(value / (sum(inventory.values()) * 100), 1)}%"
        )

    most_abundant_item: str = ""
    highest_quantity: int = 0
    least_abundant_item: str = ""
    lowest_quantity: int = 0
    first_item: bool = True

    for item, quantity in inventory.items():
        if first_item:
            most_abundant_item = item
            highest_quantity = quantity
            least_abundant_item = item
            lowest_quantity = quantity
            first_item = False
        else:
            if quantity > highest_quantity:
                most_abundant_item = item
                highest_quantity = quantity

            if quantity < lowest_quantity:
                least_abundant_item = item
                lowest_quantity = quantity

    print(
        f"Item most abundant: {most_abundant_item} "
        f"with quantity {highest_quantity}"
    )
    print(
        f"Item least abundant: {least_abundant_item} "
        f"with quantity {lowest_quantity}"
    )
    inventory.update({"sword": 99, "shield": 99})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

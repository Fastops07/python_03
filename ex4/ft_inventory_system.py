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
    keys = inventory.keys()
    for key in keys:
        print(f"'{key}'", end=" ")


if __name__ == "__main__":
    main()

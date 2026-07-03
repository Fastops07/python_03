import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            x_str: str
            y_str: str
            z_str: str
            x_str, y_str, z_str = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_str.strip())
        except ValueError as err:
            print(f"Error on parameter '{x_str.strip()}': {err}")
            continue

        try:
            y = float(y_str.strip())
        except ValueError as err:
            print(f"Error on parameter '{y_str.strip()}': {err}")
            continue

        try:
            z = float(z_str.strip())
        except ValueError as err:
            print(f"Error on parameter '{z_str.strip()}': {err}")
            continue
        return (x, y, z)


def calculate_distance(
    pos1: tuple[float, float, float], pos2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos_p1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos_p1}")
    print(f"It includes: X={pos_p1[0]}, Y={pos_p1[1]}, Z={pos_p1[2]}")

    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    distance_from_center: float = round(calculate_distance(pos_p1, center), 4)
    print(f"Distance to center: {distance_from_center}")
    print()

    print("Get a second set of coordinates")
    pos_p2: tuple[float, float, float] = get_player_pos()
    distance_between_points: float = round(
        calculate_distance(pos_p1, pos_p2), 4
    )
    print(
        "Distance between the 2 sets of coordinates: "
        f"{distance_between_points}"
    )


if __name__ == "__main__":
    main()

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordonates_str: list[str] = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
            x: float
            y: float
            z: float
            x, y, z = (float(pos.strip()) for pos in coordonates_str)
            return (x, y, z)
        except ValueError:
            print("Invalid syntax")


def calculate_distance(
    pos1: tuple[float, float, float], pos2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")

    pos_p1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos_p1}")
    print(f"It includes: X={pos_p1[0]}, Y={pos_p1[1]}, Z={pos_p1[2]}")

    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    distance_from_center: float = round(calculate_distance(pos_p1, center), 4)
    print(f"Distance to center: {distance_from_center}")

    print("Get a second set of coordinates")
    pos_p2: tuple[float, float, float] = get_player_pos()
    distance_between_points: float = round(
        calculate_distance(pos_p1, pos_p2), 4
    )
    print(f"Distance between the two points: {distance_between_points}")


if __name__ == "__main__":
    main()

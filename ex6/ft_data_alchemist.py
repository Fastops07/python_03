import random

PLAYERS: list[str] = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam",
]


def main() -> None:
    print("=== Data Alchemist ===")
    print()

    inital_players: list[str] = PLAYERS
    print(f"Initial list of players: {inital_players}")

    capitalized_players: list[str] = [
        name.capitalize() for name in inital_players
    ]
    print(f"New list with all names capitalized: {capitalized_players}")

    only_capitalize: list[str] = [
        name for name in inital_players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {only_capitalize}")

    dict_score: dict[str,int] = {
        name: random.randint(0,1000) for name in capitalized_players
    }
    print(f"Score dict: {dict_score}")

if __name__ == "__main__":
    main()

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
    print("=== Game Data Alchemist ===")
    print()

    initial_players: list[str] = PLAYERS
    print(f"Initial list of players: {initial_players}")

    capitalized_players: list[str] = [
        name.capitalize() for name in initial_players
    ]
    print(f"New list with all names capitalized: {capitalized_players}")

    already_capitalized_names: list[str] = [
        name for name in initial_players if name == name.capitalize()
    ]
    print(f"New list of capitalized names only: {already_capitalized_names}")

    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in capitalized_players
    }
    print(f"Score dict: {score_dict}")

    total_score: int = sum(score_dict.values())
    average_score: float = total_score / len(score_dict)
    print(f"Score average is {round(average_score, 2)}")

    high_score_dict: dict[str, int] = {
        name: score for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {high_score_dict}")


if __name__ == "__main__":
    main()

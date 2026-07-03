import random

ALL_ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Hidden Path Finder",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements: set[str] = set()


def gen_player_achievements() -> set[str]:
    nb_of_achievements = random.randint(5, 9)
    selected_achievements: set[str] = set(
        random.sample(ALL_ACHIEVEMENTS, nb_of_achievements)
    )
    return selected_achievements


def get_unique_for_player(
    player: Player,
    players: list[Player],
) -> set[str]:
    unique: set[str] = player.achievements

    for other_player in players:
        if other_player != player:
            unique = unique.difference(other_player.achievements)
    return unique


def get_all_distinct_achievements(players: list[Player]) -> set[str]:
    distinct_achievements: set[str] = set()
    for player in players:
        distinct_achievements = distinct_achievements.union(
            player.achievements
        )
    return distinct_achievements


def get_common_achievements(players: list[Player]) -> set[str]:
    common_achievements: set[str] = players[0].achievements
    for player in players[1:]:
        common_achievements = common_achievements.intersection(
            player.achievements
        )
    return common_achievements


def get_missing_achievements(player: Player) -> set[str]:
    all_achievements: set[str] = set(ALL_ACHIEVEMENTS)
    player_achievement: set[str] = player.achievements
    return all_achievements.difference(player_achievement)


def main() -> None:
    players: list[Player] = [
        Player("Alice"),
        Player("Bob"),
        Player("Charlie"),
        Player("Dylan"),
    ]

    print("=== Achievement Tracker System ===")
    print()

    for player in players:
        player.achievements = gen_player_achievements()
        print(f"Player {player.name}: {player.achievements}")
    print()

    all_distinct_achievements: set[str] = get_all_distinct_achievements(
        players
    )
    print(f"All distinct achievements: {all_distinct_achievements}")
    print()

    common_achievements: set[str] = get_common_achievements(players)
    print(f"Common achievements: {common_achievements}")
    print()

    for curr_player in players:
        unique: set[str] = get_unique_for_player(curr_player, players)
        print(f"Only {curr_player.name} has: {unique}")
    print()

    for curr_player in players:
        print(
            f"{curr_player.name} is missing: "
            f"{get_missing_achievements(curr_player)}"
        )


if __name__ == "__main__":
    main()

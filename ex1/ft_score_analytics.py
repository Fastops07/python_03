import sys


def build_scores_from_args(args: list[str]) -> list[int]:
    scores: list[int] = []
    for arg in args:
        try:
            converted_nb: int = int(arg)
            scores.append(converted_nb)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = build_scores_from_args(sys.argv[1:])

    if len(scores) == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    highest_score: int = max(scores)
    lowest_score: int = min(scores)
    score_range: int = highest_score - lowest_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.1f}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()

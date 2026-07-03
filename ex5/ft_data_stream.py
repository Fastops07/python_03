import typing
import random

PLAYERS: list[str] = [
    "alice",
    "bob",
    "charlie",
    "dylan",
]

ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        random_player: str = random.choice(PLAYERS)
        random_action: str = random.choice(ACTIONS)
        yield random_player, random_action


def consume_event(
    lst: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while lst:
        random_index: int = random.randint(0, len(lst) - 1)
        item: tuple[str, str] = lst[random_index]
        lst.pop(random_index)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event_generator: typing.Generator[tuple[str, str], None, None] = (
        gen_event()
    )

    player: str
    action: str
    for index in range(1000):
        player, action = next(event_generator)
        print(f"Event {index}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = [
        next(event_generator) for _ in range(10)
    ]
    print(f"Built list of 10 events: {event_list}")

    for item in consume_event(event_list):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

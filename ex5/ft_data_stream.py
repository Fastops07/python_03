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
        random_player: int = random.choice(PLAYERS)
        random_action: int = random.choice(ACTIONS)
        yield (random_player, random_action)

def consume_event(lst: list[tuple[str,str]]) -> typing.Generator[tuple[str,str], None, None]:
    while(len(lst) != 0):
        random_index: int = random.randint(0,len(lst) - 1)
        item: tuple[str,str] = lst[random_index]
        lst.pop(random_index)
        yield item


def main() -> None:
    event_generator = gen_event()

    player: str
    action: str
    for index in range(1000):
        player, action = next(event_generator)
        print(f"Event {index}: Player {player} did action {action}")

    lst: list[tuple[str, str]] = [next(event_generator) for _ in range(10)]
    print(lst)

    delete_generator = consume_event(lst)

    for index in delete_generator:
        print(next(delete_generator)) 
    print("Over", lst)
if __name__ == "__main__":
    main()

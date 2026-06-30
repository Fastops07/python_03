import sys


def main() -> None:
    argc: int = len(sys.argv)

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")

        index: int = 1
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()

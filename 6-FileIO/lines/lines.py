import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # 2) Validate file extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # 3) Open file safely
    try:
        with open(filename, "r") as file:
            # TODO: count only real code lines
            count = 0
            for line in file:
                count += 1
                # TODO: ignore blank lines and comment-only lines

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

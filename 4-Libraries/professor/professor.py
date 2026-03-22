import random


def main():
    level = get_level()  # Added () to actually run the function
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    # Note: The task usually doesn't ask for "correct!",
                    # but it's fine for testing!
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")  # Task says output "EEE" for non-numbers too
                tries += 1

        # Check if they failed after the while loop finishes
        if tries == 3:
            print(f"{x} + {y} = {x + y}")

    # Final score happens ONCE after the 10-problem loop ends
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    start = 10 ** (level - 1)
    end = (10**level) - 1
    return random.randint(start, end)


if __name__ == "__main__":
    main()

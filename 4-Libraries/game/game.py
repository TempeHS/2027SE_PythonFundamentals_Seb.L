import random
import sys  # Useful for clean exits


def main(n):  # Added 'n' here so the function knows what the level is
    print("Game started!")
    number = random.randint(1, n)
    while True:
        try:
            numguess = int(input("Guess: "))  # Standardizing the prompt
            if numguess > number:
                print("Too large!")
            elif numguess < number:
                print("Too small!")
            else:  # If it's not larger or smaller, it MUST be equal
                print("Just right!")
                break
        except EOFError:
            print("\nGoodbye!")
            sys.exit()  # Ends the program immediately
        except ValueError:
            pass  # Just ignores it and loops back to the input


# This is the part that runs first
while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            main(level)  # Pass the 'level' into the function
            break
        else:
            # We don't need a specific print here unless you want one,
            # it will just loop back anyway.
            continue

    except ValueError:
        continue  # Just loops back if they type "cat"
    except EOFError:
        print()  # Adds a newline for neatness
        break

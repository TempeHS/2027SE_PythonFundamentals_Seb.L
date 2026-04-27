def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


def is_valid(s):
    # Length must be 2 to 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if not s[:2].isalpha():
        return False

    # Only letters and numbers are allowed (no spaces or punctuation)
    if not s.isalnum():
        return False

    number_started = False

    for ch in s:
        if ch.isdigit():
            if not number_started:
                number_started = True
                # First number cannot be 0
                if ch == "0":
                    return False
        elif number_started:
            # Once numbers start, no letters may appear after
            return False

    return True


if __name__ == "__main__":
    main()

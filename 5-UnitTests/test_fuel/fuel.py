def main():
    fraction = input("Fraction: ")
    percentage = handling(fraction)
    print(f"{percentage}%")


def handling(fraction):
    try:
        # code that might crash
        numerator, denominator = fraction.split("/")
        percentage = (int(numerator) / int(denominator)) * 100
        return round(percentage)
    except ValueError:
        # runs if a ValueError occurs
        raise
    except ZeroDivisionError:
        raise
    # runs if division by zero occurs


if __name__ == "__main__":
    main()

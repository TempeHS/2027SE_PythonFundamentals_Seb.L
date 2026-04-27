from datetime import date
import inflect

p = inflect.engine()


def main():
    birth_date = get_birth_date()  # fixed: call the function
    minutes = minutes_since(birth_date)
    words = minutes_words(minutes)
    print(f"{words} minutes")


def get_birth_date():
    try:
        birth_text = input("Date of birth (YYYY-MM-DD): ").strip()
        return date.fromisoformat(birth_text)
    except ValueError:
        raise SystemExit("Invalid date")


def minutes_since(birth_date):
    days_passed = (date.today() - birth_date).days
    return days_passed * 24 * 60


def minutes_words(minutes):  # fixed: accept parameter
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()

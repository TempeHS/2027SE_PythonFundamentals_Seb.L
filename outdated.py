months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}
while True:
    date = input("Date:")
    try:
        if "/" in date:
            month, day, year = map(int, date.split("/"))

        elif "," in date:
            monthn, rest = date.split(" ", 1)
            monthn = monthn.lower().strip()

            if monthn not in months:
                continue

            day, year = rest.replace(",", "").split()
            month = months[monthn]
            day = int(day)
            year = int(year)

        else:
            continue

        if not (1 <= month <= 12 and 1 <= day <= 31):
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        continue

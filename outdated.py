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
    date = input("")
    try:
        if "/" in date:
            day, month, year = int(date.split("/", ""))

        elif "," in date:
            monthn, rest = date.split(" ", "")
            monthn = monthn.lower().strip()

            if months[monthn] not in month:
                continue

            day, year = rest.split("")
            month = months[monthn]
            day = int(day)
            year = int(year)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                print(f"{year}-{month}, {day}")
    except ValueError:
        continue

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
    date = input()
    try:
        

d1, d2, d3 = date.split("/")
date.replace("/", "")


if d2 in months:
    print(f"{d3}-{date[d2]}-{d1}")

else:
    print(f"{d3}-{d2}-{d1}")

mex = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super Burrito": 8.50,
    "super Quesadilla": 9.50,
    "taco": 3.00,
    "tortilla Salad": 8.00,
}

total = 0
while True:
    dgw = input("").strip().lower()

    if dgw == "exit":
        break

    elif dgw in mex:
        price = mex[dgw]
        total = total + price
        print(total)

    else:
        print("item not found")

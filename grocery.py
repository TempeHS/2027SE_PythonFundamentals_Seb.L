grocery = []

try:
    item = input().strip().lower
    grocery[item] += 1
    if grocery[item] == item:
        grocery[item] += 1
    else:
        print(grocery[item], item)
except ValueError:
    print("nothing")

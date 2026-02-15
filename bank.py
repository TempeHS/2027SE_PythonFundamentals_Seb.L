greeting = input("greeting ")
if greeting.startswith("Hello") or greeting.startswith("hello"):
    print("You get $0")
elif greeting.startswith("H") or greeting.startswith("h"):
    print("How about $20")
else:
    print("You get $100")

coin = int(input("Insert coin: "))
cost = 50
if coin == 15:
    cost = cost - coin
    print("Amount due:", cost)

elif coin == 10:
    cost = cost - coin
    print("Amount due:", cost)

elif coin == 25:
    cost = cost - coin
    print("Amount due:", cost)

elif coin == 5:
    cost = cost - coin
    print("Amount due:", cost)

else:
    print(cost)

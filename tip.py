pay = input("How much to pay ")
payf = float(pay)
tip = input("Enter tip percentage ")
tipf = float(tip) / 100
total = payf + (payf * tipf)
print(f"Total: $ {total:.2f}")

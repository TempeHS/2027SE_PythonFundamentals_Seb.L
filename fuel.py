fuel = input("").replace("/", " ")
print(fuel)
numerator, denominator = fuel.split()

val = (int(numerator) / int(denominator)) * 100
print(f"{val:.0f}%")

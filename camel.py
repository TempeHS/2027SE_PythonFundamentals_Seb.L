import re


user_string = input("Enter a camelCase string: ")

spaced_string = re.sub(r"([a-z])([A-Z])", r"\1 \2", user_string)

result = spaced_string.split()


print(result)

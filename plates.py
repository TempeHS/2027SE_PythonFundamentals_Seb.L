def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def mid(s):
    index = len(s) // 2

    if s[index].isdigit():
        return False
    else:
        return True


def twol(s):
    if s[0:2].isalpha():
        return True


def check(s):
    punct = (",", " ", '""')
    if s in punct:
        return False
    if s not in punct:
        return True


def is_valid(s):
    return 2 <= len(s) <= 6 and mid(s) and twol(s) and s[0] != "0"


main()

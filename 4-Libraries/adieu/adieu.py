import inflect


def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Your Name?")
            names.append(name)
        except EOFError:
            print()
            break

    output = p.join(names)
    print(f"Adieu, adieu, to {output}")

    main()

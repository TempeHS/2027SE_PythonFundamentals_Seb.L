def main():
    time_str = input("what time is it")
    total_min = convert(time_str)

    if 480 <= total_min <= 660:
        print("breakfast")

    elif 720 <= total_min <= 810:
        print("lunch")

    else:
        print("Not meal time.")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    totalmin = hours * 60 + minutes
    return totalmin


if __name__ == "__main__":
    main()

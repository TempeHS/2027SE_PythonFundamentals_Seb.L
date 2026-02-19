def main():
    time_str = input("what time is it")


def convert(time):
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)


totalmin = hours * 60 + minutes

if totalmin >= 480 and totalmin <= 660:
    print("breakfast")

import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Check for correct number of command-line arguments
    if len(sys.argv) == 1:
        # Zero arguments: select a random font
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        # Two arguments: check if the font exists
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid usage")
    else:
        # Any other number of arguments or incorrect flag
        sys.exit("Invalid usage")

    # Prompt user for text
    text = input("Input: ")

    # Set the font and output the rendered text
    figlet.setFont(font=font)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()

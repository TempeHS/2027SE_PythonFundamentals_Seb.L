import sys
from pathlib import Path
from PIL import Image, ImageOps


def valid_extension(name: str) -> bool:
    return Path(name).suffix.lower() in {".jpg", ".jpeg", ".png"}


def main():
    # 1) Argument count
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    infile = sys.argv[1]
    outfile = sys.argv[2]

    # 2) Extension checks
    if not valid_extension(infile) or not valid_extension(outfile):
        sys.exit("Invalid output")
    if Path(infile).suffix.lower() != Path(outfile).suffix.lower():
        sys.exit("Input and output have different extensions")

    # 3) Image processing (add this next)
    try:
        with Image.open(infile) as photo, Image.open("shirt.png") as shirt:
        fitted = ImageOps.fit(photo, shirt)
        # TODO: resize/crop input to shirt size with ImageOps.fit
        # TODO: paste shirt on top using mask=shirt
        # TODO: save to outfile
        pass
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()

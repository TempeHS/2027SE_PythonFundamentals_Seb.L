from fpdf import FPDF


def main():
    # Prompt user for their name
    name = input("What's your name? ")

    # Create a PDF object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add title
    pdf.set_font("Arial", size=24)
    pdf.cell(0, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    # Add shirt image
    pdf.image("shirtificate.png", x=50, y=80, w=110)

    # Add user's name on the shirt
    pdf.set_text_color(255, 255, 255)  # White text
    pdf.set_font("Arial", size=16)
    pdf.text(x=75, y=140, txt=f"{name} took CS50")

    # Save the PDF
    pdf.output("shirtificate.pdf")
    print("Shirtificate created as 'shirtificate.pdf'!")


if __name__ == "__main__":
    main()

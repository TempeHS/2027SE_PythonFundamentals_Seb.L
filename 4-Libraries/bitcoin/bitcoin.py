import sys
import requests


def main():
    # 1. Check for command-line argument
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # 2. Try to convert the input to a float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3. Query the API and handle potential web errors
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # Ensure we got a successful 200 OK response
        response.raise_for_status()

        # Parse the JSON "nesting dolls"
        data = response.json()
        price = data["bpi"]["USD"]["rate_float"]

        # 4. Calculate total cost
        total_cost = n * price

        # 5. Output with formatting: , for thousands and .4f for 4 decimals
        print(f"${total_cost:,.4f}")

    except requests.RequestException as e:
        sys.exit(f"Actual error: {e}")


if __name__ == "__main__":
    main()

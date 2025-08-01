def main():
    # Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2700,
        "AMZN": 3300,
        "MSFT": 300
    }

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Please enter a valid stock symbol.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
            continue
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total_investment = 0
    print("\nYour Portfolio:")
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}")

    print(f"\nTotal Investment Value: ${total_investment}")

    save_option = input("Do you want to save the portfolio to a file? (yes/no): ").lower()
    if save_option == "yes":
        file_type = input("Enter file type to save (txt/csv): ").lower()
        filename = input("Enter filename (without extension): ")
        if file_type == "txt":
            with open(f"{filename}.txt", "w") as f:
                f.write("Stock Portfolio\n")
                for stock, quantity in portfolio.items():
                    investment = stock_prices[stock] * quantity
                    f.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${investment}\n")
                f.write(f"Total Investment Value: ${total_investment}\n")
            print(f"Portfolio saved to {filename}.txt")
        elif file_type == "csv":
            import csv
            with open(f"{filename}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price per Share", "Investment"])
                for stock, quantity in portfolio.items():
                    investment = stock_prices[stock] * quantity
                    writer.writerow([stock, quantity, stock_prices[stock], investment])
                writer.writerow([])
                writer.writerow(["Total Investment Value", "", "", total_investment])
            print(f"Portfolio saved to {filename}.csv")
        else:
            print("Unsupported file type. Portfolio not saved.")
    else:
        print("Portfolio not saved.")

if __name__ == "__main__":
    main()

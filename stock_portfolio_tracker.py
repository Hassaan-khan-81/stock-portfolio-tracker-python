
"""## Initialize Stock Prices

### Subtask:
Defining a hardcoded dictionary containing stock symbols and their respective prices.

**Reasoning**:
The subtask requires defining a hardcoded dictionary named `stock_prices` with stock symbols and their corresponding prices. This code block will create and display the dictionary.
"""

stock_prices = {
    'AAPL': 170.00,
    'GOOGL': 1500.50,
    'MSFT': 250.75,
    'AMZN': 100.20,
    'TSLA': 800.00
}

print("Stock prices dictionary created:")
print(stock_prices)

"""## Collect User Stock Inputs

### Subtask:
Prompting the user to enter stock names and quantities, storing them for calculation.

**Reasoning**:
The subtask requires prompting the user for stock names and quantities, validating the input against the predefined stock prices, and storing the valid entries in a list. This step will implement the interactive input loop.
"""

portfolio = []

print("\nEnter your stock holdings. Type 'done' when finished.")
while True:
    stock_symbol = input("Enter stock symbol (e.g., AAPL) or 'done': ").strip().upper()

    if stock_symbol == 'DONE':
        break

    if stock_symbol not in stock_prices:
        print(f"Error: Stock symbol '{stock_symbol}' not found in our records. Please try again.")
        continue

    while True:
        try:
            quantity = float(input(f"Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print("Quantity must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a numeric value.")

    portfolio.append({'stock': stock_symbol, 'quantity': quantity})
    print(f"Added {quantity} shares of {stock_symbol} to your portfolio.")

print("\nPortfolio input complete.")
print("Your current portfolio:")
for item in portfolio:
    print(f"  Stock: {item['stock']}, Quantity: {item['quantity']}")

"""## Calculate Portfolio Value

### Subtask:
Compute the total investment value based on the user's inputs and the defined stock prices.

**Reasoning**:
Calculate the total portfolio value by iterating through the user's portfolio, looking up each stock's price, and summing up the individual stock values.
"""

total_portfolio_value = 0.0

for item in portfolio:
    stock_symbol = item['stock']
    quantity = item['quantity']
    price = stock_prices.get(stock_symbol) # Use .get() for safer lookup

    if price is not None:
        value = quantity * price
        total_portfolio_value += value
        print(f"  {stock_symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
    else:
        print(f"  Warning: Price for {stock_symbol} not found. This stock will not be included in total value.")

print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")

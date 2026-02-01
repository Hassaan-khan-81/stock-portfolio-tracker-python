# 📈 Stock Portfolio Tracker - Python

A simple stock portfolio tracker that calculates total investment value based on manually defined stock prices. Built in Python as part of my internship (Task 2).

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-yellow.svg)

---

## 📋 Task Description

**Goal:** Build a simple stock tracker that calculates total investment based on manually defined stock prices.

### Simplified Scope:
- ✅ User inputs stock names and quantity
- ✅ Uses a hardcoded dictionary to define stock prices
- ✅ Displays total investment value
- ✅ Input validation and error handling

---

## 🎯 Features

- **Predefined Stock Prices**: AAPL, GOOGL, MSFT, AMZN, TSLA
- **Interactive Input**: Add multiple stocks to your portfolio
- **Input Validation**: Validates stock symbols and quantities
- **Portfolio Summary**: Shows individual stock values and total
- **Error Handling**: Gracefully handles invalid inputs

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Hassaan-khan-81/stock-portfolio-tracker-python.git

# Navigate to the directory
cd stock-portfolio-tracker-python

# Run the tracker
python stock_portfolio_tracker.py
```

---

## 🔑 Key Programming Concepts Used

This project demonstrates fundamental Python concepts:

### 1. 📚 Dictionary
```python
stock_prices = {
    'AAPL': 170.00,
    'GOOGL': 1500.50,
    'MSFT': 250.75,
    'AMZN': 100.20,
    'TSLA': 800.00
}
```
- Stores stock symbols as **keys** and prices as **values**
- Efficient lookup using `stock_prices.get(symbol)`
- Used to check if a stock exists: `if symbol in stock_prices`

### 2. 📥📤 Input/Output
```python
# Getting user input
stock_symbol = input("Enter stock symbol: ").strip().upper()

# Formatted output
print(f"  {stock_symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
```
- `input()` function to get user data
- `.strip()` removes whitespace, `.upper()` converts to uppercase
- f-strings for formatted output with decimal places

### 3. ➕ Basic Arithmetic
```python
value = quantity * price
total_portfolio_value += value
```
- Multiplication to calculate individual stock value
- Addition to sum up total portfolio value
- Using `+=` operator for accumulation

### 4. 🔄 Loops (While & For)
```python
# While loop for continuous input
while True:
    stock_symbol = input("Enter stock symbol: ")
    if stock_symbol == 'DONE':
        break

# For loop to iterate through portfolio
for item in portfolio:
    value = item['quantity'] * stock_prices[item['stock']]
```
- **While loop**: Allows user to add multiple stocks
- **For loop**: Iterates through portfolio to calculate values

### 5. ⚠️ Error Handling (try-except)
```python
try:
    quantity = float(input("Enter quantity: "))
    if quantity <= 0:
        print("Quantity must be positive.")
except ValueError:
    print("Invalid quantity. Please enter a number.")
```
- Catches invalid numeric inputs
- Validates quantity is positive
- Provides user-friendly error messages

---

## 📁 Project Structure

```
stock-portfolio-tracker-python/
│
├── stock_portfolio_tracker.py    # Main tracker file
└── README.md                     # Project documentation
```

---

## 📸 Sample Output

```
Stock prices dictionary created:
{'AAPL': 170.0, 'GOOGL': 1500.5, 'MSFT': 250.75, 'AMZN': 100.2, 'TSLA': 800.0}

Enter your stock holdings. Type 'done' when finished.
Enter stock symbol (e.g., AAPL) or 'done': AAPL
Enter quantity for AAPL: 10
Added 10.0 shares of AAPL to your portfolio.

Enter stock symbol (e.g., AAPL) or 'done': TSLA
Enter quantity for TSLA: 5
Added 5.0 shares of TSLA to your portfolio.

Enter stock symbol (e.g., AAPL) or 'done': done

Portfolio input complete.
Your current portfolio:
  Stock: AAPL, Quantity: 10.0
  Stock: TSLA, Quantity: 5.0

  AAPL: 10.0 shares @ $170.00 = $1700.00
  TSLA: 5.0 shares @ $800.00 = $4000.00

Total Portfolio Value: $5700.00
```

---

## 💹 Available Stocks

| Symbol | Price ($) |
|--------|-----------|
| AAPL   | 170.00    |
| GOOGL  | 1500.50   |
| MSFT   | 250.75    |
| AMZN   | 100.20    |
| TSLA   | 800.00    |

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Built-in modules only** - No external dependencies

---

## 📚 Learning Outcomes

By building this project, I learned:
1. How to use **dictionaries** for key-value data storage
2. Handling user **input/output** with validation
3. Performing **arithmetic operations** for calculations
4. Using **loops** for iteration and continuous input
5. Implementing **error handling** with try-except blocks
6. Working with **lists of dictionaries** for complex data

---

## 👨‍💻 Author

**Internship Task 2**

---

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning!

---

## 🌟 Acknowledgments

- This project was created as part of my internship program

---

*Happy Investing! 📊*

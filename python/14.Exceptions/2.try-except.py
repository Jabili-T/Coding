#handling arithmetic exception using try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

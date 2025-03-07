#prog with finally 
try:
    print("Trying...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught division by zero!")
finally:
    print("This always executes!")

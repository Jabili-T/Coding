#Multiple except Blocks
try:
    x = int("abc")  
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid conversion of string to integer!!!!!!!!!!!")
except Exception as e:
    print(f"Other error: {e}")

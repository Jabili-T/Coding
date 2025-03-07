''' Same Name, Same Parameters is Not Possible
Python does not allow two methods with the same name and same parameters. The last one will overwrite the first.'''
class Example:
    def show(self, a, b):
        print(f"First method: {a}, {b}")

    def show(self, x, y):  # Overwrites the first method
        print(f"Second method: {x}, {y}")

obj = Example()
obj.show(10, 20)  # Calls the second method

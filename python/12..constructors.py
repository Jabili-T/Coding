#===================================================================ASSIGNMENT-12
# Parent class with multiple constructors
class Parent:
    def __init__(self, name="Parent Default", age=None):  # Default, one-arg, and two-arg constructor
        self.name = name  # Public attribute
        self._protected_attr = "Protected Parent Attribute"  # Protected attribute
        self.__private_attr = "Private Parent Attribute"  # Private attribute
        self.age = age
        if age is None:
            print(f"Default Constructor: Name = {self.name}")
        elif age is not None and name != "Parent Default":
            print(f"Two-Arg Constructor: Name = {self.name}, Age = {self.age}")
        else:
            print(f"One-Arg Constructor: Name = {self.name}")

    def show_attributes(self):
        print(f"Public Name: {self.name}")
        print(f"Protected Attribute: {self._protected_attr}")
        print(f"Private Attribute: {self.__private_attr}")

# Child class that calls both default and argument constructors of the Parent class
class Child(Parent):
    def __init__(self, name="Child Default", age=None, roll_no=101):
        super().__init__(name, age)  # Calling Parent's constructor
        self.roll_no = roll_no  # Additional attribute in child
        print(f"Child Constructor: Name = {self.name}, Age = {self.age}, Roll No = {self.roll_no}")

    # Demo access to parent attributes
    def access_parent_data(self):
        print(f"Accessing Parent Public Name: {self.name}")
        print(f"Accessing Parent Protected Attribute: {self._protected_attr}")
        # Private attribute access via name mangling
        print(f"Accessing Parent Private Attribute: {self._Parent__private_attr}")
print("\n*** Creating Parent Objects***")
p1 = Parent()  # Default Constructor
p2 = Parent("Zoya")  # One-Arg Constructor
p3 = Parent("Zoya", 21)  # Two-Arg Constructor
print("\n*** Creating Child Object***")
c1 = Child("Zoya", 21, 102)  # Calling both Parent & Child Constructor
print("\n*** Accessing Parent Attributes from Child ***")
c1.access_parent_data()


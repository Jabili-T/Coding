#Assignment-7
# A, B and C are classes 
# A is a super class. B is a sub class of A. C is a sub class of B.  
# Create three methods in each class, 2 methods are specific to each class and third 
# method (override method) should be in all three Classes A, B and C 

class A:
    def __init__(self):
        self.category = "Class A - Superclass"

    def method1(self):
        print("Method 1 in Class A")

    def method2(self):
        print("Method 2 in Class A")

    def commonMethod(self):
        print("Overridden Method in Class A")

class B(A):
    def __init__(self):
        super().__init__()
        self.category = "Class B - Subclass of A"

    def method3(self):
        print("Method 3 in Class B")

    def method4(self):
        print("Method 4 in Class B")

    def commonMethod(self):
        print("Overridden Method in Class B")

class C(B):
    def __init__(self):
        super().__init__()
        self.category = "Class C - Subclass of B"

    def method5(self):
        print("Method 5 in Class C")

    def method6(self):
        print("Method 6 in Class C")

    def commonMethod(self):
        print("Overridden Method in Class C")

# Create a class with main method. Create an object for each class A, B and C in main  
# method and call every method of each class using its own object/instance. 

if __name__ == "__main__":
    print("=== Object of Class A ===")
    objA = A()
    objA.method1()
    objA.method2()
    objA.commonMethod()
    print("Instance variable of A:", objA.category)  
    print()

    print("=== Object of Class B ===")
    objB = B()
    objB.method1()
    objB.method2()
    objB.method3()
    objB.method4()
    objB.commonMethod()
    print("Instance variable of B:", objB.category)  
    print()

    print("=== Object of Class C ===")
    objC = C()
    objC.method1()
    objC.method2()
    objC.method3()
    objC.method4()
    objC.method5()
    objC.method6()
    objC.commonMethod()
    print("Instance variable of C:", objC.category)  
    print()

    # Call an overridden method with super class reference to B and C class’s objects 

    print("=== Calling Overridden Method Using Superclass Reference ===")
    refA = B()
    refA.commonMethod()

    refB = C()
    refB.commonMethod()
    print()

    # Runtime Polymorphism with Data Members/Instance variables, Repeat the above  
    # process only for data members 

    print("=== Runtime Polymorphism with Data Members ===")
    refA = B()
    print("Superclass reference (A) pointing to B - category:", refA.category)

    refB = C()
    print("Superclass reference (B) pointing to C - category:", refB.category)

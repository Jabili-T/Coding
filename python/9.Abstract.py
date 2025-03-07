#====================ASSIGNMENT-9========
from abc import ABC, abstractmethod

class AbstractClass(ABC):  
    @abstractmethod
    def abstract_method(self):  
        pass  
    
    def non_abstract_method(self):  
        return "This is a non-abstract method"

class ChildClass(AbstractClass):  
    def abstract_method(self):  
        return "Implemented abstract method"

    def call_abstract(self):
        obj = ChildClass()
        return obj.abstract_method()

    def call_non_abstract(self):
        obj = ChildClass()
        return obj.non_abstract_method()

# Create an instance of the child class
child = ChildClass()

# 1. Access non-abstract method from abstract class
print(child.non_abstract_method())  

# 2. Call abstract method from the child class
print(child.abstract_method())

# 3. Create an instance inside the child class and call the abstract method
print(child.call_abstract())

# 4. Create an instance inside the child class and call the non-abstract method
print(child.call_non_abstract())

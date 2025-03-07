#assignment-8
class BankAccount:
    def __init__(self, acc_number, balance):
        self.__account_number = acc_number  # Private field
        self.__balance = balance  # Private field

    def __display_balance(self):  # Private method
        print("Your balance is:", self.__balance)

    def show_balance(self):
        self.__display_balance()

class Customer(BankAccount):
    def __init__(self, acc_number, balance):
        super().__init__(acc_number, balance)

    def try_access_private(self):
        print("Cannot access private account details directly.")

ramesh_account = BankAccount("123456789", 10000)
ramesh_account.show_balance()

suresh_account = Customer("987654321", 5000)
suresh_account.try_access_private()


class Employee:
    def __init__(self, name, salary):
        self._name = name  # Protected field
        self._salary = salary  # Protected field

    def _display_salary(self):  # Protected method
        print(f"{self._name}'s salary is {self._salary}")

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def access_protected(self):
        print("Manager accessing protected employee details:")
        print(f"Name: {self._name}")
        self._display_salary()

employee1 = Employee("Ramesh", 50000)
print("Accessing protected field within the same package:", employee1._name)
employee1._display_salary()

manager1 = Manager("Suresh", 80000)
manager1.access_protected()


class Book:
    def __init__(self, title, author):
        self.title = title  # Public field
        self.author = author  # Public field

    def display_book(self):  # Public method
        print(f"Book: {self.title} by {self.author}")

class LibraryMember(Book):
    def __init__(self, title, author, member_name):
        super().__init__(title, author)
        self.member_name = member_name  # Public field

    def borrow_book(self):  # Public method
        print(f"{self.member_name} borrowed '{self.title}' by {self.author}")

book1 = Book("Mahabharata", "Vyasa")
print("Accessing public field:", book1.title)
book1.display_book()

member1 = LibraryMember("Ramayana", "Valmiki", "Priya")
member1.borrow_book()

#FUNCTIONS
# 1. Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 100:")
for i in range(1, 101):
    if is_prime(i):
        print(i, end=" ")

# 2. Temperature Converter
def convert_temp(value, unit):
    if unit.lower() == 'c':
        return (value * 9/5) + 32
    elif unit.lower() == 'f':
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

print(convert_temp(100, 'c'))
print(convert_temp(212, 'f'))

# 3. Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#CLASSES
# 4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

r = Rectangle(5, 5)
print(r.area(), r.perimeter(), r.is_square())

# 5. BankAccount Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

acc = BankAccount("Aaron", 1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())

# 6. Book Class
class Book:
    def __init__(self, title, author, price, in_stock):
        self.title = title
        self.author = author
        self.price = price
        self.in_stock = in_stock

    def sell(self, quantity):
        if quantity <= self.in_stock:
            self.in_stock -= quantity
        else:
            raise ValueError("Not enough stock")

b = Book("Python", "Author A", 500, 10)
b.sell(3)
print(b.in_stock)

# 7. Student Grade System
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

s = Student("Aaron", [80, 90, 70])
print(s.average(), s.grade())

#INHERITANCE
# 8. Person → Employee
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(self.name, self.age, self.emp_id, self.salary)

e = Employee("AARON SAM", 21, "101", 50000)
e.display_info()

# 9. Vehicle → Car, Bike
class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def description(self):
        return f"{self.name} has {self.wheels} wheels."

class Car(Vehicle):
    def __init__(self, name, wheels, fuel_type):
        super().__init__(name, wheels)
        self.fuel_type = fuel_type

    def description(self):
        return f"{self.name} runs on {self.fuel_type}."

class Bike(Vehicle):
    def __init__(self, name, wheels, is_geared):
        super().__init__(name, wheels)
        self.is_geared = is_geared

    def description(self):
        return f"{self.name} is {'geared' if self.is_geared else 'non-geared'}."

c = Car("Honda", 4, "Petrol")
b = Bike("Hero", 2, True)
print(c.description())
print(b.description())

# 10. Polymorphism with Animals
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())







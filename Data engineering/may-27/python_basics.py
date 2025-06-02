# VARIABLES,DATA TYPES,OPERATORS
#1.Digit Sum Calculator
num = input("Enter a number: ")
sum_digit = sum(int(digit) for digit in num)
print("Digit sum:", sum_digit)
#2.Reverse a 3-digit Number
a = input("Enter a 3-digit number: ")
print("Reversed number:", a[::-1])
#3.Unit Converter (meters to cm, feet, inches)
m = float(input("Enter distance in meters: "))
print("Centimeters:", m * 100)
print("Feet:", m * 3.28084)
print("Inches:", m * 39.3701)
#4.Percentage Calculator
marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
total = sum(marks)
average = total / 5
percentage = (total / 500) * 100
print("Total:", total, "Average:", average, "Percentage:", percentage)
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: D")

#CONDITIONALS

#5.Leap Year Checker
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
#6.Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
menu = input("Enter operator : ")

if menu== '1':
    print("Result:", a + b)
elif menu == '2':
    print("Result:", a - b)
elif menu == '3':
    print("Result:", a * b)
elif menu == '4':
    print("Result:", a / b)
else:
    print("Invalid operator")
#7.Triangle Validator
a, b, c = map(int, input("Enter 3 sides: ").split())
if a + b > c and b + c > a and a + c > b:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
#8.Bill Splitter with Tip
bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))
total_with_tip = bill + (bill * tip_percent / 100)
print("Amount per person:", round(total_with_tip / people, 2))


#LOOPS
#9.Prime Numbers Between 1 and 100
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
#10.Palindrome Checker
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#11.Fibonacci Series (First N Terms)
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
#12.Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#13.Number Guessing Game
import random
num = random.randint(1, 100)
guess = -1
while guess != num:
    guess = int(input("Guess a number: "))
    if guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High")
    else:
        print("Correct!")
#14.ATM Machine Simulation
balance = 10000
while True:
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        amt = float(input("Enter amount: "))
        balance += amt
    elif choice == '2':
        amt = float(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds")
    elif choice == '3':
        print("Balance:", balance)
    elif choice == '4':
        break
    else:
        print("Invalid choice")
#15.Password Strength Checker
import re
pwd = input("Enter password: ")
if (len(pwd) >= 8 and
    re.search(r"[A-Z]", pwd) and
    re.search(r"[a-z]", pwd) and
    re.search(r"\d", pwd) and
    re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd)):
    print("Strong Password")
else:
    print("Weak Password")
#16.Find GCD (Greatest Common Divisor)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b
print("GCD is:", a)








# Python Full-Spectrum Assessment

# Section 1: Python Basics & Control Flow

 #creation of dataset using pandas
# Dataset 1: employees.csv
import pandas as pd
employees_data = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["Ali", "Neha", "Ravi", "Sara", "Vikram"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 70000, 52000],
    "JoiningDate": ["2021-03-15", "2022-01-10", "2020-07-23", "2023-05-19", "2022-09-30"]
}
employees_df = pd.DataFrame(employees_data)
employees_df.to_csv("employees.csv", index=False)
print("employees data created successfully.")
# Dataset 2: projects.csv
projects_data = {
    "ProjectID": [101, 102, 103, 104],
    "EmployeeID": [2, 3, 3, 5],
    "ProjectName": ["AI Chatbot", "ERP System", "Payroll Automation", "Cloud Migration"],
    "HoursAllocated": [120, 200, 150, 100]
}
projects_df = pd.DataFrame(projects_data)
projects_df.to_csv("projects.csv", index=False)
print("projects Data created successfully.")
###########################################################
# Q1: Print all odd numbers between 10 and 50
for i in range(11, 50, 2):
    print(i, end=' ')
print()
# Q2: Check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year=int(input("Enter a year: "))
a=is_leap_year(year)
print(f"{year} is a leap year: {a}")
# Q3: Count how many times 'a' appears in a string
s= "Aaron sam is a Data engineer"
count = s.lower().count('a')
print("Occurrences of 'a':", count)
# Q4: Create dictionary from two lists
keys = ['a', 'b', 'c']
values = [100, 200, 300]
my_dict = dict(zip(keys, values))
print(my_dict)
##############################################################
#Section 2: Collections (Lists, Tuples, Sets, Dicts)
# Q5: Salaries processing
salaries = [50000, 60000, 55000, 70000, 52000]
max_salary = max(salaries)
avg_salary = sum(salaries) / len(salaries)
above_avg = [s for s in salaries if s > avg_salary]
sorted_desc = sorted(salaries, reverse=True)
print("Max:", max_salary)
print("Above average:", above_avg)
print("Sorted Desc:", sorted_desc)
# Q6: Set operations
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
set_a = set(a)
set_b = set(b)
print("Set A:", set_a)
print("Set B:", set_b)
print("Difference (A - B):", set_a - set_b)
###########################################################
#Section 3: Functions & Classes
# Q7: Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}: {self.salary}")

    def is_high_earner(self):
        return self.salary > 60000
# Q8: Project class (inherits from Employee)
class Project(Employee):
    def __init__(self, name, salary, project_name, hours_allocated):
        super().__init__(name, salary)
        self.project_name = project_name
        self.hours_allocated = hours_allocated
# Q9: Instantiate and check high earners
e1 = Employee("Ali", 50000)
e2 = Employee("Sara", 70000)
e3 = Employee("Ravi", 55000)
for i in [e1, e2, e3]:
    i.display()
    print("High Earner:", i.is_high_earner())
###########################################################
#Section 4: File Handling
# Q10: Write IT employee names to file
#already pandas is being imported
df = pd.read_csv("employees.csv")
it_employees = df[df["Department"] == "IT"]["Name"]
with open("it_employees.txt", "w") as f:
    for name in it_employees:
        f.write(name + "\n")
# Q11: Read a text file and count words
with open("it_employees.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Word count:", len(words))
###########################################################
#Section 5: Exception Handling
# Q12: Square number with error handling
try:
    num = int(input("Enter a number: "))
    print("Square is", num ** 2)
except ValueError:
    print("That's not a number!")
# Q13: Handle ZeroDivisionError
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))
###########################################################
#Section 6: Pandas – Reading & Exploring CSVs
# Q14: Load CSVs
emp_df = pd.read_csv("employees.csv")
proj_df = pd.read_csv("projects.csv")
# Q15: Display first 2 rows, unique departments, avg salary by dept
print(emp_df.head(2))
print(emp_df["Department"].unique())
print(emp_df.groupby("Department")["Salary"].mean())
# Q16: Add TenureInYears column
from datetime import datetime
current_year = datetime.now().year
emp_df["JoiningYear"] = pd.to_datetime(emp_df["JoiningDate"]).dt.year
emp_df["TenureInYears"] = current_year - emp_df["JoiningYear"]
print(emp_df[["Name", "TenureInYears"]])
###########################################################
#Section 7: Data Filtering, Aggregation, Sorting
# Q17: Filter IT employees with salary > 60000
filtered = emp_df[(emp_df["Department"] == "IT") & (emp_df["Salary"] > 60000)]
print(filtered)
# Q18: Group by department
dept_stats = emp_df.groupby("Department").agg(
    Count=('EmployeeID', 'count'),
    TotalSalary=('Salary', 'sum'),
    AvgSalary=('Salary', 'mean')
)
print(dept_stats)
# Q19: Sort by salary descending
print(emp_df.sort_values(by="Salary", ascending=False))
###########################################################
#Section 8: Joins & Merging
# Q20: Merge employees and projects on EmployeeID
merged_df = pd.merge(emp_df, proj_df, on="EmployeeID", how="inner")
print(merged_df)
# Q21: Employees not working on any project
unassigned = pd.merge(emp_df, proj_df, on="EmployeeID", how="left")
print(unassigned[unassigned["ProjectID"].isna()])
# Q22: Add TotalCost column
unassigned["TotalCost"] = unassigned.apply(
    lambda row: row["HoursAllocated"] * (row["Salary"] / 160)
    if pd.notnull(row["HoursAllocated"]) else 0,
    axis=1
)
print(unassigned[["Name", "ProjectName", "TotalCost"]])
###########################################################







#LISTS

#1.List of Squares
squares = [x**2 for x in range(1, 21)]
print(squares)
#2-Second Largest Number
b= [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in b:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print("Second Largest:", second)
#3.Remove Duplicates
l = [1, 2, 2, 3, 1, 4]
result = []
for i in l:
    if i not in result:
        result.append(i)
print(result)
#4.Rotate List Right by k
l = [1, 2, 3, 4, 5]
k = 2
rotated = l[-k:] + l[:-k]
print(rotated)
#5.List Compression (Even Numbers Doubled)
n = [1, 2, 3, 4, 5, 6]
compressed = [i * 2 for i in n if i % 2 == 0]
print(compressed)

# TUPLES
#6.Swap Values
def swap_tuples(t1, t2):
    return t2, t1
print(swap_tuples((1, 2), (3, 4)))
#7.Unpack Tuples
student = ("Aaron", 20, "AI&DS", "A")
name, age, branch, grade = student
print(f"{name}, aged {age}, is in {branch} branch and got grade {grade}")
#8.Tuple to Dictionary
tup = (("a", 1), ("b", 2))
d = dict(tup)
print(d)

#SETS
#9.Common Items
a = set(input("List 1: ").split())
b = set(input("List 2: ").split())
print("Common:", a & b)
#10.Unique Words in Sentence
s=input("enter a sentence:")
unique=set(s.split())
print(unique)
#11.Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)
#12.Subset Checker
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

# DICTIONARIES
#13. Frequency counters
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
#14.Student Grade Book
students = {}
for _ in range(3):
    name = input("Name: ")
    marks = int(input("Marks: "))
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    else:
        grade = "C"
    students[name] = grade
query = input("Enter name to check grade: ")
print(students.get(query, "Student not found"))
#15.Merge Two Dictionaries
d1 = {"a": 5, "b": 3}
d2 = {"a": 2, "c": 4}
for k, v in d2.items():
    d1[k] = d1.get(k, 0) + v
print(d1)
#16.Inverted Dictionary
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
print(inv)
#17.Group Words by Length
words = ["towel", "brush", "car", "door", "cat"]
grouped = {}
for word in words:
    l = len(word)
    grouped.setdefault(l, []).append(word)
print(grouped)





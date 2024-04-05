import math

# Question 1 write your name
print("""
_____   ____  ___         ___
|   \\   \\__/  | |         | |
|___/    ||   | |    __   | |
|   \\    ||   | |_  /  \\  | |_
\\___/    []   |___| \\_/ \\ |___|
""")

# Question 2 calculate area of a triangle from 3 sides

print("Hello I am an AI that will ask for sides of a triangle and will calculate the area.")
a = float(input("What is the length of side a?:   "))
b = float(input("What is the length of side b?:   "))
c = float(input("What is the length of side c?:   "))
s = (a+b+c)/2
area = s * (s-a) * (s-b) * (s-c)
areaTrue = round(math.sqrt(area), 2)
print("The area of the triangle is:   ", areaTrue)

# Question 3 provide a budgeting plan for a persons budget
print("Hello I am here to provide you with a budgeting plan for your monthly budget.")
budget = float(input("What is your monthly budget?:   "))
rent = round(0.35 * budget, 2)
food = round(0.3 * budget, 2)
clothing = round(0.22 * budget, 2)
entertainment = round(0.13 * budget, 2)
print("""
for your various needs the following budgeting plan has been set up for you:
Rent:   $""", rent, """(35%)
Food:   $""", food, """(30%)
Clothing:   $""", clothing, """(22%))
Entertainment:   $""", entertainment, """(13%))
I hope this plan is satisfactory for you.
""")

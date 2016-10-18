# PAGE 91
# NO BOXES

# PAGE 92
# BOX 1
print(4 == 4)
print(4 != 4)
print(4 < 5)
print(4 >= 3)
print("A" < "B")

# PAGE 93
# BOX 1
import math

area = int(input("Enter the area: "))
if area > 0:
    radius = math.sqrt (area / math.pi)
    print("The radius is", radius)
else:
    print("Error: the area must be a positive number")

# BOX 2
# Format/syntax of an if-else statement

# BOX 3
# Semantics of an if-else statement

# PAGE 94
# BOX 1
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first
print ("Maximum:", maximum)
print ("Minimum:", minimum)

# BOX 2
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print("Maximum:", max(first, second))
print("Minimum:", min(first, second))

# BOX 3
# Format of an if statement (without else)

# PAGE 95
# BOX 1
# Semantics of an if statement (without else)

# BOX 2
"""
if x < 0:
    x = -x
"""

# PAGE 96
# BOX 1
number = int(input("Enter the numeric grade: "))
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print("The letter grade is", letter)

# BOX 2
# Format of an if-elif-else statement

# PAGE 97
# BOX 1
number = int(input("Enter the numeric grade: "))
if number > 100:
    print("Error: grade must be between 100 and 0")
elif number < 0:
    print("Error: grade must be between 100 and 0")
else:
    if number > 89:
        letter = 'A'
    elif number > 79:
        letter = 'B'
    elif number > 69:
        letter = 'C'
    else:
        letter = 'F'
    print("The letter grade is", letter)

# BOX 2
number = int(input("Enter the numeric grade: "))
if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
else:
    if number > 89:
        letter = 'A'
    elif number > 79:
        letter = 'B'
    elif number > 69:
        letter = 'C'
    else:
        letter = 'F'
    print("The letter grade is", letter)

# BOX 3
number = int(input("Enter the numeric grade: "))
if number >= 0 and number <= 100:
    if number > 89:
        letter = 'A'
    elif number > 79:
        letter = 'B'
    elif number > 69:
        letter = 'C'
    else:
        letter = 'F'
    print("The letter grade is", letter)
else:
    print("Error: grade must be between 100 and 0")

# PAGE 98
# BOX 1
# Truth table for or, not, and and

# PAGE 99
# BOX 1
A = True
B = False
print(A and B)
print(A or B)
print(not A)

# PAGE 100
# BOX 1
count = int(input("Enter the count: "))
sum1 = int(input("Enter the sum1: "))
if count > 0 and sum1 / count > 1:
    print("Average > 10")
else:
    print("Count = 0 or average <= 10")

# PAGE 101
# NO BOXES

# PAGE 102
# BOX 1
# Format of a while loop

# PAGE 103
# BOX 1
# Semantics of a while loop

# PAGE 104
# BOX 1
sum1 = 0.0
data = input("Enter a number or just enter to quit: ")
while data != "":
    number = float(data)
    sum1 += number
    data = input("Enter a number or just enter to quit: ")
print("The sum1 is", sum1)

# BOX 2
sum1 = 0
for count in range(1, 100001):
    sum1 += count
print(sum1)

sum1 = 0
count = 1
while count <= 100000:
    sum1 += count
    count += 1
print(sum1)

# PAGE 105
# BOX 1
for count in range(10, 0, -1):
    print (count,)

count = 10
while count >= 1:
    print(count,)
    count -= 1

# BOX 2
sum1 = 0.0
while True:
    data = input("Enter a number or just enter to quit: ")
# CONTINUED ON PAGE 106

# PAGE 106
# BOX 1
# CONTINUED FROM PAGE 105
    if data == "":
        break
    number = float(data)
    sum1 += number
print("The sum1 is", sum1)

# BOX 2
while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print(number)

# BOX 3
# OUTPUT FROM BOX 2
"""
Enter the numeric grade: 101
Error: the grade must be between 100 and 0
Enter the numeric grade: -1
Error: the grade must be between 100 and 0
Enter the numeric grade: 45
45
"""

# PAGE 107
# BOX 1
done = False
while not done:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        done = True
    else:
        print("Error: Grade must be between 100 and 0")
print(number)

# BOX 2
import random
for roll in range(10):
    print(random.randint(1, 6),)

# PAGE 108
# BOX 1
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    else:
        print("You've got it in", count, "tries!")
        break

# PAGE 109
# NO BOXES

# PAGE 110
# NO BOXES

# PAGE 111
# NO BOXES

# PAGE 112
# BOX 1
"""
Program: newton.py
Author: Ken

Compute the square root of a number.

1. The input is a number.

2. The outputs are the program's estimate of the square root
   using Newton's method of succesive approximations, and
   Python's own estimate using math.sqrt.
"""

import math

# Receive the input number from the user
x = int(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0
# CONTINUED ON PAGE 113

# PAGE 113
# BOX 1
# CONTINUED FROM PAGE 112
# Perform the succesive approximations
while True:
    estimate = (estimate + x / estimate) /2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break
# Output the result
print("The program's estimate:", estimate)
print("Python's estimate:   ", math.sqrt(x))

# NO BOXES FROM PAGES 114 - 120

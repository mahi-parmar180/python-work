#print message
x="Hello world!"
print(x)

#Add two numbers
num1=input("Enter first number: ")
num2 = input("Enter second number: ")
sum = int(num1) + int(num2)
print("Sum is:", sum)

#Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")

import math
print("Value of PI is:", math.pi)

PI = 3.14   # constant value
print("Constant value is:", PI)

num = int(input("Enter a number: "))
square = num * num
print("Square of the number is:", square)

radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius * radius
print("Area of the circle is:", area)

num=12
print(type(num))

import math
num = int(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Square:", math.pow(num, 2))
print("Value of PI:", math.pi)

import math
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
result = math.pow(base, exponent)
print(base, "raised to the power", exponent, "is:", result)

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")










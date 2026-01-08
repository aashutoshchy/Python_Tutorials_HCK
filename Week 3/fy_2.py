"""
Write a python program that asks user’s input and sum three
numbers. However, if two values are equal, the sum will be zero. Hint:
You might want to use logical operator.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum_num = num1+num2+num3

if num1==num2 or num2==num3 or num1==num3:
    print("Sum is: 0")
else:
    print("Sum is: ", sum_num)

"""
Write a python program to calculate the sum of three given
numbers. If the values are equal then print three time their sum.
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum_num = num1+num2+num3

if num1 == num2 == num3:
    print("Three time of sum is: ", sum_num*3)

else:
    print("Sum is: ", sum_num)

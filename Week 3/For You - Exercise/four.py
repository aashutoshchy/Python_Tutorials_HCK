"""
Write a program that takes in two numbers and
displays the product of the two numbers if both numbers are positive,
otherwise it returns "Numbers must be positive".
"""

first_num = int(input("Enter first mumber: "))
sec_num = int(input("Enter first mumber: "))

if first_num < 0 or sec_num < 0:
    print("Numbers must be positive")
else:
    print("Product is: ", first_num * sec_num)

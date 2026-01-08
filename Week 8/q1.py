# Write a Python program to ask the user for 2 numbers. Then print out the result of the first number divided by the second number. Handle the 'ZeroDivision Error' exception to give a meaningful output.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    division = num1/num2
    print(f"{num1} Divided by {num2} is {division}")

except ZeroDivisionError:
    print("Cannot divided by Zero")

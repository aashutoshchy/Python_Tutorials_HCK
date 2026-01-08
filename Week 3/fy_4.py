"""
Write a python program that asks user's bar order. If the order
contains alcohol, the program should check the customer's ID. If the ID
states that the customer is under 18 years, the program should display
the legal drinking age law and end. If the customer is over 18, the
program should serve alcoholic drink and exit
"""

order = input("What do you want to order? \n> ").lower()

if order == "alcohol":
    age = int(input("Enter you age:"))
    if age>18:
        print("Here is your Alcohol.")
    else:
        print("The legal drinking age law is 18.")

else:
    print("Here is your", order)

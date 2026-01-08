"""
Develop a program which prompts user to ask the temperature in
Celsius and convert that into Fahrenheit with a display message.
And Explain how the flow of code is sequential. (Hint: (Celsius * 9/5)+ 32)
"""

cel = float(input("Enter temperature in Celsius: "))
fahren = (cel*9/5)+32
print("In Fahreinheit: ", fahren)

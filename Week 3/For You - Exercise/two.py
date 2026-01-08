"""
Write a program that accepts percentage form the user and display the
grade according to the following. [Percentage and GPA should be of herald college]
"""

percentage = float(input("Enter your percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid Percentage")
elif percentage >= 70:
    print("First-class 'A'")
elif percentage >= 60 and percentage < 70:
    print("Upper second-class 'B'")
elif percentage >= 50 and percentage < 60:
    print("Lower second-class 'B'")
elif percentage >= 40 and percentage < 50:
    print("Third-Class 'B'")
else:
    print("Fail")

"""
Accept any city from the user and display tourist attraction of that city
"""

city = input("Enter the city: ").lower()

if city == "kathmandu":
    print("Pashupatinath Temple")
elif city == "pokhara":
    print("Fewa Lake")
elif city == "nepalgunj":
    print("Bageshwori Temple")
else:
    print("Birgunj Ghanta Ghar")

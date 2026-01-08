'''
Develop a system where multiple branches has been used to
control the flow of earthquake destruction simulation.
'''

richter_val = int(input("Enter Earthquake Richter: "))

if richter_val > 8:
    print("Most structures fall")
elif richter_val >= 7:
    print("Many Building destroyed")
elif richter_val >= 6:
    print("Many Building Considerably damaged, some collapsed.")
elif richter_val >= 4.5:
    print("Damaged to poorly constructed Building")
else:
    print("No Destruction of Building")


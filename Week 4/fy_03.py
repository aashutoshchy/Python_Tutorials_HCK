user_input = input("Enter a number: ")
sum = 0

while user_input != '':
    sum += int(user_input)
    user_input = input("Enter a number: ")

print("Sum is: ", sum)
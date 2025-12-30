while userInput != 0:
    def printMenu():
        print("Enter 1 for simple Calculator: ")
        print("Enter 2 for Factorial: ")
        print("Enter 3 for simple mean/Median: ")
        print("Enter 0 to exit: ")
        
        userInput = input()
        
        if userInput == 1:
            calculator()
        elif userInput == 2:
            factorial()
        else:
            median()

printMenu()


def calculator():
    firstNum = int(input("Enter firstNum: "))
    secNum = int(input("Enter secNum: "))
    operations = input("Enter your operations(+, -, *, /): ")

    if operations == '+':
        sum(firstNum, secNum)
    if operations == '-':
        diff(firstNum, secNum)
    if operations == '*':
        prod(firstNum, secNum)
    if operations == '/':
        div(firstNum, secNum)


userInput()

# For Calculator

def sum(firstNum, secNum):
    print("Sum is: ", firstNum + secNum);

def diff(firstNum, secNum):
    print("Difference is: ", firstNum - secNum);

def prod(firstNum, secNum):
    print("Product is: ", firstNum * secNum);

def div(firstNum, secNum):
    print("Division is: ", firstNum / secNum);

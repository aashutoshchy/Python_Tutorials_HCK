def calculateSimpleInterest(principle, rate, time):
    return (principle * rate * time / 100)



principle = int(input("Enter principle: "))
rate = float(input("Enter Rate: "))
time = int(input("Enter Time: "))

si = calculateSimpleInterest(principle, rate, time);
print("Simple Interest is: ", si)

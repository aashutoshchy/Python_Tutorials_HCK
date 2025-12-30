posCount = 0;
negCount = 0;
zeroCount = 0;


while(cont != 'N'):

    userWants = int(input("Enter a number: "));
    if userWants < 0:
        negCount += 1
    elif userWants > 0:
        posCount += 1
    else
        zeroCount += 1
    
    
    cont = input("Do you want to continue? (Y/N): ")
    



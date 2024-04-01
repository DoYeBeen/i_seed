def addNumber(num) :

    if(num < 2) : return 1
    else: return num + addNumber(num-1)

print(addNumber(100))
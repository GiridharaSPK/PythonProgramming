def toDecimal(b):
    d=0
    i=1
    while(b>=1):
        r=b%10
        b=b//10
        d=d+r*i
        i=i*2
    return d

def toBinary(d):
    b=0
    i=1
    while(d>=1):
        r=d%2
        d=d//2
        b=b+r*i
        i=i*10
    return b

def conversionSwitch():
    switch=int(input("Enter \"1\" to convert \'to decimal\' or \"2\" to convert \'to binary\': "))
    if(switch==1):
        n=int(input("Enter a binary number for conversion to Decimal: "))
        print(toDecimal(n))
        return
    elif(switch==2):
        n=int(input("Enter a decimal number for conversion to Binary: "))
        print(toBinary(n))
        return

conversionSwitch()

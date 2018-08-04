# multiply two values and print the result
def multiply(a,b):
    c=a*b
    print(c)
def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def div(a,b):
    c=a/b
    print(c)
def rem(a,b):
    c=a%b
    print(c)
def exp(a,b):
    c=a**b
    print(c)

def multab(d):
    for b in range(1,11):
        c=b*d
        print(b," * ",d," = ",c)
multab(3)

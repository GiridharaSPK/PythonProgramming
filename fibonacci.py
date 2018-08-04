def fibonacci(i):
    if(i<=1):
        return(i)
    else:
        return(fibonacci(i-1)+fibonacci(i-2))

n=int(input("Enter a number: "))
print("-------------")
for i in range(1,n+1):
    print(fibonacci(i))

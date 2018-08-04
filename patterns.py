star="*"
space=" "

print("Pattern 1")
limit=int(input("Enter the number: "))
def pattern1():
    for i in range (1,limit+1):
        print(star*i)

pattern1()
print("-------")

print("Pattern 2")
def pattern2():
    for i in range (1,limit+1):
        print(space*(limit-i),star*i)

pattern2()

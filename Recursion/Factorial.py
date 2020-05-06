def myFact(n):
    if n==1:
        return 1
    else:
        return n*myFact(n-1)

num=int(input("Enter a number: "))
if num<0:
    print("No negative numbers")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial of",num,"is",myFact(num))

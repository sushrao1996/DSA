def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
count=int(input("Enter the count: "))
if(count<=0):
    print("Please enter a count greater than 2")
else:
    sum=0
    for i in range(count):
        print(fib(i),end=" ")
        
   

        

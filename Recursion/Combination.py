def fact(n):
    if n<0:
        print("No negative numbers")
    elif n<=1:
        return 1
    else:
        return n*fact(n-1)
def combination(n,r):
    return (fact(n)/(fact(r)*fact(n-r)))
n=5
r=3
print(int(combination(n,r)))

def power(base,exp):
    if exp==1:
        return base
    else:
        return base*power(base,exp-1)
base=int(input("Enter the base: "))
exp=int(input("Enter the exp: "))
print(power(base,exp))

A=[5,4,1,8,3]
for i in range(len(A)):
    min_index=i
    for j in range(i+1,len(A)):
        if A[min_index]>A[j]:
            min_index=j
    A[i],A[min_index]=A[min_index],A[i]
for i in A:
    print(i,end=" ")

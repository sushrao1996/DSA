def mergesort(arr):
    if len(arr)>1:
        midpoint=len(arr)//2
        LEFT=arr[:midpoint]
        RIGHT=arr[midpoint:]

        mergesort(LEFT)
        mergesort(RIGHT)

        i=j=k=0

        while i<len(LEFT) and j<len(RIGHT):
            if LEFT[i]<RIGHT[j]:
                arr[k]=LEFT[i]
                i+=1
            else:
                arr[k]=RIGHT[j]
                j+=1
            k+=1
        while i<len(LEFT):
            arr[k]=LEFT[i]
            i+=1
            k+=1
        while j<len(RIGHT):
            arr[k]=RIGHT[j]
            j+=1
            k+=1
myArray=[15,5,24,8,1,3,16,10,20]
mergesort(myArray)
for i in myArray:
    print(i,end=" ")
        
        

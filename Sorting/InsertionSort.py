def insertionSort(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        j=i-1
        while j>=0 and val<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=val
myArray=[9,6,7,3,2]
insertionSort(myArray)
for i in myArray:
    print(i,end=" ")

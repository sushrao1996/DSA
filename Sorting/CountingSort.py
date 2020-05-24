def countingsort(arr,high):
    counter=[0]*(high+1)
    for i in arr:
        counter[i]+=1
    startpoint=0
    for i in range(len(counter)):
        while counter[i]>0:
            arr[startpoint]=i
            startpoint+=1
            counter[i]-=1
arr=[5,3,2,3,6,1]
countingsort(arr,6)
for i in arr:
    print(i,end=" ")

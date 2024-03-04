# Print True is there is a valid pair present else print false.

arr=[2,-1,0,3,2,5,7]
n=int(input("Enter the Number to check pair: "))
count=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==n:
            count+=1
            break

if count!=0:
    print('True')
else:
    print("False")
# print the maximum value of (abs(arr[i]-arr[j]+i-j)) Possible.

arr=[3,9,8,4,1]
max=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if max<abs(arr[i]-arr[j])+i-j:
            max=abs(arr[i]-arr[j])+i-j

print(max)
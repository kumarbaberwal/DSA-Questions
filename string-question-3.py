str=input("Enter a string: ").upper()
count=0
for i in range(len(str)//2):
    if str[i]!=str[len(str)-i-1]:
        count+=1

if count==0:
    print("Input String is palindrome!")    
else:
    print("Input String is not palindrome!")
        
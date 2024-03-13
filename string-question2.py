string="abfk"
for i in range(1,len(string)+1):
    if i<len(string):
        dif=str(ord(string[i])-ord(string[i-1]))
        print(string[i-1]+dif,end="")
    else:
        print(string[i-1],end="")
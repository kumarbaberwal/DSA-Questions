string="abfk"
for i in range(0,len(string)):
    dif=str(ord(string[i])-ord(string[i-1]))
    print(string[i-1]+dif,end="")
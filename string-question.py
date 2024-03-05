string="AbCs"
for i in range(len(string)):
    if ord(string[i])<97:
        print(chr(ord(string[i])+32),end="")
    else:
        print(chr(ord(string[i])-32),end="")

# A="a"
# print(ord(A))
# print(chr(ord(A)+3))
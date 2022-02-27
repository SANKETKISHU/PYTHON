ch=input("enter the line")
str=''
for i in ch:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
     str=str+chr(ord(i)+32)
    else:
     str=str+i
print(str)

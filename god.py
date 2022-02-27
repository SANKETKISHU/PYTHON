c=-1
a=input("enter the line:")
print(chr(ord(a[c+1])-32))
for ch in a:
    c=c+1
    if ch==' ':
       print(chr(ord(a[c+1])-32),end='')
    else:
       print(a[c+1],end='')

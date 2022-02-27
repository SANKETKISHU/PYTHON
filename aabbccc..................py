b=0
l=input("enter the characters:")
length=len(l)
for i in range(0,length-1):
 for j in range(0,b):
    print(l[i],end='')
 b=b+1

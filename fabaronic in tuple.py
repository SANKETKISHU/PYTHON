tpl=()
lst=[]
a=0
b=1
c=0
k=1
n=int(input("enter the number:"))
while k<=n+2:
     lst.append(c)
     a=b
     b=c
     c=a+b
     k=k+1
tpl=tuple(lst)
print(tpl)

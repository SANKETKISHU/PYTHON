s=0
av=0
l=[]
for i in range(1,5+1):
    a=tuple(eval(input("enter the tuple:")))
    for j in a:
        s=s+j
    av=s/len(a)
    print(a,s,av)
    l.append(a)
print(l)
print(tuple(l))

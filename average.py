lst=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
slc1=lst[5:15:2]
slc2=lst[::4]
sum=avg=0
print("slice1")
for a in slc1:
    sum+=a
    print(a,end='')
print()
print("sum of elements of slice1:",sum)
print("slice2")
sum=0
for a in slc2:
    sum+=a
    print(a,end='')
print()
avg=sum/len(slc2)
print("avrage of elements slice 2:",avg)

a=int(input("enter the value:"))
c=0
for val in range(2,a):
    if a%val==0:
      c=c+1
if c==0:
   print("prime no.")

else:
   print("not prime")
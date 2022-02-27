a=int(input("enter the number:"))
c=0
for val in range(1,a+1):
    if a%val==0:
        c=c+1
if c==2:
  print("prime number")
else:
  print("no prime number")

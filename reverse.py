r=0
n=int(input("enter number:"))
while n>0:
  m=n%10
  r=(r*10)+m
  n=n//10
print(r)

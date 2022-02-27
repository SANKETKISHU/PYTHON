str=input("enter the string:")
s=0
s1=0
for a in str:
     if a.isdigit()==True:
       s1=s1*10+int(a)
       s=s+int(a)
     elif a.isdigit()==False:
        print(a)
print(str)
print(s)
if s==0:
        print("has no digit")
        

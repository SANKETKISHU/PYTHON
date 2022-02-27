ch=''
string1=input("enter the string:")
length=len(string1)
i=0
for a in range(-1,(-length-1),-1):
    print(string1[i],"\t",string1[a])
    ch=ch+string1[a]
    i+=1
if ch==string1:
 print("number is pallindrom number")
else:
 print("nbumber is not pallindrom number")

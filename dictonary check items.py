D1=eval(input("enter the value:"))
c=0
for key ,value in D1.items():
    c=0
    for key1,value1 in D1.items():
        if value==value1:
            c=c+1
    if c>1:
        break
if c>1:
    print("2 keys have same same value:")
else:
     print("2 keys have not same same value:")
    
    

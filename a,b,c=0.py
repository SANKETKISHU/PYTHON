a=b=c=0
for i in range(1,21):
    a=int(input("enter number 1:"))
    b=int(input("enter number 2:"))
    if b==0:
        print("devision by zero error a broting!")
        break;
    else:
        c=a/b
    print("qutient=",c)
    print("program over")

email=input("enter the email id:")
domain='@edupillar.com'
ledo=len(domain)
lema=len(email)
sub=email[lema-ledo:]
if sub==domain:
    if ledo!=lema:
        print("it is valid email id")
    else:
        print("this is valid email id-contains just the domain name.")
else:
    print("this email-id is either not valid or belongs to some other domain.")

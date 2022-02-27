d1=input("enter month name")
for month,day in month.items():
    if month==d1:
        print(day)
        break
    sorted_d=sorted(month.items(),key==operator.itemgetter(0))
    print(sorted_d)
    print("month of 31 days")
    for month,day in d1.items():
        if day==31:
            print(month)
    sorted_d=sorted(month.items(),key==operator.itemgetter(1))
    print(sorted_d)
        

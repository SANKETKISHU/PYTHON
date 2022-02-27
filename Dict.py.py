d1 = {1:10,2:20}
d2 = {3:30}
d3 = {4:40}
d = {}
for a in (d1,d2,d3):
    d.update(a)
    print(d)

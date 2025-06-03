a,b,c,d=list(map(int, input("").split()))
la=[]
lb=[]
if a<0 and b>0:
    la.append(0)
la.append(a)
la.append(b)
if c<0 and d>0:
    lb.append(0)
lb.append(c)
lb.append(d)
m=a*c
for i in la:
    for j in lb:
        o=i*j
        if o>m:
            m=o
print(m)
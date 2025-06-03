t1,t2 = map(int,input().split())
c1,c2 = map(int,input().split())
d1,d2 = map(int,input().split())
hosei = 0
if t1*c1>t1*d1:
    a1=c1
    a2=c2
    b1=d1
    b2=d2
else:
    a1,a2,b1,b2=d1,d2,c1,c2
if t1*a1+t2*a2 > t1*b1+t2*b2:
    print(0)
    exit()
elif t1*a1+t2*a2 == t1*b1+t2*b2:
    print("infinity")
else:
    # print((t1*(a1-b1))//(t2*(b2-a2)) + 1,t1*(a1-b1),t2*(b2-a2))
    if t2*(b2-a2) % (t2*(b2-a2)-t1*(a1-b1)) == 0:
        hosei = 1
    print((t2*(b2-a2)) // (t2*(b2-a2)-t1*(a1-b1))*2-1-hosei)
    # print((t2*(a2-b2)))
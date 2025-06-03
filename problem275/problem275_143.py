a,b=map(int,input().split())
dic={1:3*10**5,2:2*10**5,3:1*10**5}
c=0
if a in dic and b in dic:
    if a==1 and b==1:
        c+=dic[a]+dic[b]+4*10**5
        print(c)
    else:
        c+=dic[a]+dic[b]
        print(c)

elif a in dic and b not in dic:
    c+=dic[a]
    print(c)


elif b in dic and a not in dic:
    c+=dic[b]
    print(c)

else:
    print(c)

X,Y,Z=map(int,input().split())
l=[X,Y,Z]

l[0],l[1]=l[1],l[0]
l[0],l[2]=l[2],l[0]

print(*l)

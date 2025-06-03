l=list(map(int,input().split()))

l.sort()

if l[0]==l[1]==l[2] or l[0]!=l[1]!=l[2]:
    print("No")
else:
    print("Yes")

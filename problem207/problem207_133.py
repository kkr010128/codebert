l=[]
for i in range(3):
    l.append(list(map(int,input().split())))
d=list(zip(*l))
s=[]
f=0
n=int(input())
for i in range(n):
    s.append(int(input()))
for i in range(3):
    c=0
    for j in range(3):
        if(l[i][j] in s):
            c+=1
    if(c==3):
        f=1
        break
if(l[1][1] in s and l[0][0] in s and l[2][2] in s):
    f=1
if(l[0][2] in s and l[1][1] in s and l[2][0] in s):
    f=1
for i in range(3):
    c=0
    for j in range(3):
        if(d[i][j] in s):
            c+=1
    if(c==3):
        f=1
        break
if(f==1):
    print("Yes")
else:
    print("No")

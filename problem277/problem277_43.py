H,W,K=map(int,input().split())
s=[]
for i in range(H):
    S=input()
    s.append(S)
a=[[0 for i in range(W)] for j in range(H)]
tmp=-1
flag=False
chk=[0 for _ in range(W)]
for w in range(W):
    count=0
    for h in range(H):
        if not flag:
            if s[h][w]=="#":
                tmp=w
                flag=True
        if s[h][w]==".":
            count+=1
    if count==H:
        chk[w]=1
num=0
flag=True
f=True
for w in range(W):
    if w<tmp:
        continue
    if chk[w]==0:
        num+=1
    f=True
    for h in range(H):
        if chk[w]==0:
            if s[h][w]=="#":
                if flag:
                    num=1
                    flag=False
                if f:
                    pass
                    f=False
                else:
                    num+=1
                a[h][w]=num
            else:
                a[h][w]=num
        else:
            a[h][w]=a[h][w-1]
if tmp!=0:
    for w in range(tmp):
        for h in range(H):
            if (tmp-1-w)<0:
                break
            a[h][tmp-1-w]=a[h][tmp-w]
for i in range(H):
    print(*a[i])
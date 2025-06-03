H,W,K=map(int,input().split())

L=[]
E=[0 for i in range(W+2)]
L.append(E)
for i in range(H):
    l=[0]+list(input())+[0]
    L.append(l)
L.append(E)

#print(L)
cnt=1
for i in range(1,H+1):
    for j in range(1,W+1):
        if L[i][j]=="#":
            L[i][j]=cnt
            cnt+=1
#print(L)
for i in range(1,H+1):
    num=0
    for j in range(1,W+1):
        if num>0 and L[i][j]==".":
            L[i][j]=num
        elif L[i][j]!=".":
            num=L[i][j]
    num=0
    for j in range(1,W+1):
        if L[i][W+1-j]!=".":
            num=L[i][W+1-j]
        elif num!=0 and L[i][W+1-j]==".":
            L[i][W+1-j]=num
        
for i in range(1,H):
    if L[i+1][1]==".":
        L[i+1]=L[i]
        
for i in range(1,H):
    if L[H-i][1]==".":
        L[H-i]=L[H-i+1]


for i in range(1,H+1):
    print(*L[i][1:W+1])

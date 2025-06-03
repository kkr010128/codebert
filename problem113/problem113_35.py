d=int(input())
C=[int(i) for i in input().split()]
s=[[int(i) for i in input().split()] for q in range(d)]

sco=0
L=[0 for i in range(26)]
ans=[]

#calc
for i in range(d):
    mayou=0
    est=s[i][0]+C[0]*(i+1-L[0])
    for p in range(1,26):
        if s[i][p]+C[p]*(i+1-L[p]) > est:
            mayou=p
            est=s[i][p]+C[p]*(i+1-L[p])
    ans.append(mayou)
    L[mayou]=i+1
    print(mayou+1) #output

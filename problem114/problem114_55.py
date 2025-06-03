D=int(input())
c=[int(i) for i in input().split()]
a=[]
for i in range(D):
    a.append([int(i) for i in input().split()])

last=[0 for i in range(26)]
zoku=0
for d in range(D):
    t=int(input())
    zoku+=a[d][t-1]
    last[t-1]=d+1
    for i in range(26):
        zoku-=c[i]*(d+1-last[i])
    print(zoku)
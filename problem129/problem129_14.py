N=int(input())
A=list(map(int,input().split()))
A.sort()

F=[0]*(10**6+11)
# 0:OK/未調査 1:NG 2:調査した頂点 3:二度調査した頂点

for a in A:
    if F[a]==1:
        continue
    if F[a]==2:
        F[a]=1
        continue
    elif F[a]==0:
        F[a]=2
    k=2*a
    while k<=10**6+1:
        F[k]=1
        k+=a
            
res=0
for a in A:
    if F[a]==2:
        res+=1
print(res)
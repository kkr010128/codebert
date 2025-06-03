X,Y,A,B,C=map(int,input().split())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
R=list(map(int,input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
P.append(float("inf"))
Q.append(float("inf"))
ans=sum(P[:X]+Q[:Y])
rfinish=False
gfinish=False
r,g,f=X-1,Y-1,0
while f<C and (R[f]>P[r] or R[f]>Q[g]):
    if P[r]<Q[g]:
        ans=ans-P[r]+R[f]
        r-=1
        f+=1
    else:
        ans=ans-Q[g]+R[f]
        g-=1
        f+=1
print(ans)


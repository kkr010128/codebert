from operator import itemgetter
n=int(input())
xl=[list(map(int,input().split()))for i in range(n)]
R=[(xl[i][0]-xl[i][1],xl[i][0]+xl[i][1]) for i in range(n)]
r=sorted([(R[i][0],R[i][1]) for i in range(n)],key=itemgetter(1))
s=r[0][1]
ans=1
for i in range(n-1):
    if r[i+1][0]>=s:
        s=r[i+1][1]
        ans+=1
print(ans)
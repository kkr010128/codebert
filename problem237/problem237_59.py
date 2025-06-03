N=int(input())
xl=[list(map(int,input().split()))for _ in range(N)]
arms={}
for x,l in xl:
    arms[x-l]=0
    arms[x+l]=0
for x,l in xl:
    arms[x-l]+=1
    arms[x+l]-=1
point={}
for x,l in xl:
    point[x-l]=[]
    point[x+l]=[]
for x,l in xl:
    point[x-l].append(x+l)

ans=N
K=sorted(arms.keys())
now=0
count=[]
for k in K:
    now+=arms[k]
    for kk in point[k]:
        count.append(kk)
    for i in range(count.count(k)):
        count.remove(k)
    if now>=2:
        ans-=now-1
        now=1
        C=sorted(count)[::-1]
        for c in C[:-1]:
            arms[c]+=1
            count.remove(c)

print(ans)
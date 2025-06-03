N=int(input())
arms=[list(map(int,input().split())) for _ in range(N)]
points=[]
for i in range(N):
    points.append([arms[i][0]-arms[i][1],arms[i][0]+arms[i][1]])
#print(points)
points.sort(key=lambda x:x[1])
#print(points)
nowr=-float("inf")
cnt=0
for i in points:
    l,r=i
    if nowr<=l:
        nowr=r
        cnt=cnt+1
print(cnt)


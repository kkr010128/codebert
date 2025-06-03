N=int(input())
xl=[]
for _ in range(N):
    x,l=map(int,input().split())
    xl.append([x+l,2*l])
xl.sort()
r=-10**9
ans=0

for i in range(N):
    if xl[i][0]-xl[i][1]>=r:
        ans+=1
        r=xl[i][0]

print(ans)
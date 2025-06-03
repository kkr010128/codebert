n=int(input())
xl=[list(map(int, input().split())) for _ in range(n)]

rl=[]
for x,l in xl:
    right=x-l
    left=x+l
    rl.append([right,left])
rl.sort(key=lambda x: x[1])
# print(rl)

cnt=0
pos=-float('inf')
for i in range(n):
    if rl[i][0]>=pos:
        pos=rl[i][1]
        cnt+=1
print(cnt)


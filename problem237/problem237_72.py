n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
L.sort(key=lambda x:x[0]+x[1])
seen=-10**10
cnt=0
for i in range(n):
    if seen<=L[i][0]-L[i][1]:
        seen=L[i][0]+L[i][1]
        cnt+=1
print(cnt)
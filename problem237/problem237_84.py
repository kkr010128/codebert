n = int(input())
xl = []
for i in range(n):
    x,l = map(int,input().split())
    xl.append([x-l,x+l])
xl.sort(key = lambda x: x[1])
ans = 0
arm = -10**18
for i in range(n):
    if arm<=xl[i][0]:
        ans += 1
        arm = xl[i][1]
print(ans)
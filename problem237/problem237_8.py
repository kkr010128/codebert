from operator import itemgetter
n = int(input())
lis = []
for _ in range(n):
    x,l = map(int,input().split())
    lis.append([x-l,x+l])
lis.sort(key = itemgetter(1))
ans = 0
last = -float("inf")
for i in range(n):
    if lis[i][0] >= last:
        ans += 1
        last = lis[i][1]
print(ans)
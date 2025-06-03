N = int(input())
A = []
for i in range(N):
    x,y = map(int, input().split())
    A.append([x+y,x-y])
A.sort()
now = -float('inf')
ans = 0
for a,b in A:
    if b>=now:
        ans += 1
        now = a
print(ans)
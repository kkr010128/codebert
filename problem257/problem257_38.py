n = int(input())
a = list(map(int, input().split()))
c = 1
ans = 0
for i in range(n):
    if a[i] == c:
        c += 1
    else:
        ans += 1
if c>1:
    print(ans)
else:
    print(-1)

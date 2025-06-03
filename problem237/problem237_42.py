N = int(input())
R = []
for i in range(N):
    x, l = map(int, input().split())
    R.append((x+l, x-l))
R.sort()
ans = 0
now = -(10 ** 9 + 1)
for (r, l) in R:
    if now <= l:
        ans += 1
        now = r
print(ans)

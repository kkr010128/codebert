N = int(input())
XL = [list(map(int, input().split())) for i in range(N)]
LR = [[x - l, x + l] for x, l in XL]

LR.sort(key=lambda x: x[1])

ans = 0
prev = -float("INF")
for l, r in LR:
    if prev <= l:
        ans += 1
        prev = r

print(ans)
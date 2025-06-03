N = int(input())
XL = [list(map(int, input().split())) for x in range(N)]

XL = sorted(XL, key=lambda x: x[0]+x[1])

cnt = 0
prev_right = -10**9+10
for x, l in XL:
    left = x - l
    right = x + l
    if left >= prev_right:
        cnt += 1
        prev_right = right

print(cnt)

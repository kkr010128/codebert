import sys
input = sys.stdin.readline
n = int(input())
info = [0] * n
for i in range(n):
    x, l = map(int, input().split())
    info[i] = [x+l, x, l]

info.sort()
ans = 1
right = info[0][1] + info[0][2]
for i in range(1, n):
    if right <= info[i][1] - info[i][2]:
        ans += 1
        right = info[i][1] + info[i][2]
print(ans)
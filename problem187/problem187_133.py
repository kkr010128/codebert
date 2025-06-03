import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,x,y = map(int, input().split())

ans = [0] * n
for i in range(1, n + 1):
    for j in range(1 + i, n + 1):
        a = abs(i - x) + abs(j - y) + 1
        b = abs(i - j)
        c = min(a, b)
        ans[c] += 1

for i in range(1, n):
    print(ans[i])

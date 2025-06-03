import sys
input = sys.stdin.readline

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]
AB.sort()
ans = 0
if N & 1:
    l = AB[N//2][0]
    AB.sort(key=lambda x: x[1])
    ans = AB[N // 2][1] - l + 1
else:
    l = (AB[N // 2][0], AB[N // 2 - 1][0])
    AB.sort(key=lambda x: x[1])
    r = (AB[N // 2][1], AB[N // 2 - 1][1])
    ans = sum(r) - sum(l) + 1
print(ans)
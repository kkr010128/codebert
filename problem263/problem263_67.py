from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
INF = 10 ** 9 + 7

D = defaultdict(int)
for a in A:
    for i in range(61):
        # a の i ビット目がたっているか否か
        D[1 << i] += bool(a & (1 << i))

ans = 0
for key, value in D.items():
    ans += key * value * (N - value)
    ans %= INF

print(ans % INF)
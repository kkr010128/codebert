import sys
def input():
    return sys.stdin.readline().strip()

n, d, a = map(int, input().split())

x = []
h = {} # x:h
for _ in range(n):
    i, j = map(int, input().split())
    x.append(i)
    h[i] = j
x.sort()
x.append(x[-1] + 2*d + 1)

# attackで累積和を用いる
ans = 0
attack = [0 for _ in range(n+1)]
for i in range(n):
    attack[i] += attack[i-1]
    if attack[i] >= h[x[i]]:
        continue

    if (h[x[i]] - attack[i]) % a == 0:
        j = (h[x[i]] - attack[i]) // a
    else:
        j = (h[x[i]] - attack[i]) // a + 1
    attack[i] += a * j
    ans += j

    # 二分探索で、x[y] > x[i] + 2*d、を満たす最小のyを求める
    # start <= y <= stop
    start = i + 1
    stop = n
    k = stop - start + 1
    while k > 1:
        if x[start + k//2 - 1] <= x[i] + 2*d:
            start += k//2
        else:
            stop = start + k//2 - 1
        k = stop - start + 1
    attack[start] -= a * j

print(ans)
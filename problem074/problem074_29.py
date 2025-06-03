N, K = map(int, input().split())

area = []
for i in range(K):
    L, R = map(int, input().split())
    area.append((L, R))

area.sort()
d = [0] * N
a = [0] * N


def func(pos):
    for l, r in area:
        if pos + l - 1 < N:
            a[pos + l-1] += d[pos]
        if pos + r < N:
            a[pos + r] -= d[pos]
    d[pos+1] = (d[pos] + a[pos]) % 998244353


d[0] = 1
a[0] = -1
for i in range(0, N-1):
    func(i)

print(d[N-1] % 998244353)

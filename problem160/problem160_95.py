import itertools

n, m, q = map(int, input().split())
a, b, c, d = [0] * q, [0] * q, [0] * q, [0] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

aa = [i for i in range(1, m+1)]
maxv = -1
for i in itertools.combinations_with_replacement(aa, n):
    cnt = 0
    for j in range(q):
        if i[b[j]-1] - i[a[j]-1] == c[j]:
            cnt += d[j]
    maxv = max(maxv, cnt)

print(maxv)
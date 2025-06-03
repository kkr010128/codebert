N, K = [int(v) for v in input().split()]

links = []
for k in range(K):
    L, R = [int(v) for v in input().split()]
    links.append((L, R))

links = sorted(links, key=lambda x: x[1])

count = [1]
sub = [0, 1]
subtotal = 1

for i in range(1, N):
    v = 0
    for l, r in links:
        r2 = i - l + 1
        l2 = i - r
        if l2 < 0:
            l2 = 0
        if r2 >= 0:
            v += sub[r2] - sub[l2]

    count.append(v % 998244353)
    subtotal = (subtotal + v) % 998244353
    sub.append(subtotal )

print(count[-1])

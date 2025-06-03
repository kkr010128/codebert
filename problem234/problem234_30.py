n = int(input())
d = dict()
for i in range(1, n+1):
    t = i
    tail = t % 10
    while t >= 10:  # head, tail nomi miru.
        t //= 10
    head = t
    d[(head, tail)] = d.get((head, tail), 0) + 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        temp = d.get((i,j), 0) * d.get((j,i), 0)
        # print(i, j, temp, d.get((i, j)), d.get((j, i)))
        ans += temp
print(ans)
N, M, *PS = open(0).read().split()
N, M = [int(_) for _ in [N, M]]
cor = [0] * (N + 1)
pen = [0] * (N + 1)
for p, s in zip(PS[::2], PS[1::2]):
    p = int(p)
    if cor[p] == 1:
        continue
    if s == 'AC':
        cor[p] = 1
    else:
        pen[p] += 1
ans = [0, 0]
for i in range(1, N + 1):
    if cor[i] == 0:
        continue
    ans[0] += 1
    ans[1] += pen[i]
print(*ans)

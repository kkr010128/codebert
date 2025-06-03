K = int(input())


def dfs(d, n, buf):
    buf.append(n)

    if d == 10:
        return

    lsd = n % 10

    if lsd != 0:
        dfs(d + 1, n * 10 + lsd - 1, buf)

    dfs(d + 1, n * 10 + lsd, buf)

    if lsd != 9:
        dfs(d + 1, n * 10 + lsd + 1, buf)


buf = []

for n in range(1, 10):
    dfs(1, n, buf)

print(sorted(buf)[K - 1])

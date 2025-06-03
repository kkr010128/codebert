n, m, q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(q)]


def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return

    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)


ans, tempAns = 0, 0
for tempA in combinations_with_replacement(range(1, m + 1), n):
    tempAns = 0
    for a in A:
        if tempA[a[1] - 1] - tempA[a[0] - 1] == a[2]:
            tempAns += a[3]
    ans = max(ans, tempAns)
print(ans)
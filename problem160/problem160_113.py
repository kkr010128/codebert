import itertools

n, m, q = map(int, input().split())
abcd = [tuple(map(int, input().split())) for _ in range(q)]

ls = itertools.combinations_with_replacement([i + 1 for i in range(m)], n)

ans = 0
for A in ls:
    total = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            total += d
    ans = max(ans, total)
print(ans)

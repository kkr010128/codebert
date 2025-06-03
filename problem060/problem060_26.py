n, m, l = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
B = [tuple(map(int, input().split())) for _ in range(m)]
B_T = [tuple(r) for r in zip(*B)]
for L in ((sum((a*b for a, b in zip(ai, bj))) for bj in B_T) for ai in A):
    print(*L)
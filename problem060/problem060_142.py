n, m ,l = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for j in range(m)]
c = [[sum(ak*bk for ak, bk in zip(ai, bj)) for bj in zip(*b)] for ai in a]

for ci in c:
    print(*ci)
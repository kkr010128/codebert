n, m = list(map(int, input().split()))

mat = [list(map(int, input().split())) for _ in range(n)]
vec = [int(input()) for _ in range(m)]

for v in mat:
    print(sum(a * b for a, b in zip(v, vec)))
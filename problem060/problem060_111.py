n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(m)]
for ARow in A:
    result = []
    for BCol in zip(*B):
        result.append(sum([ARow[i] * BCol[i] for i in range(m)]))
    print(*result)
n,m,l = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n)]
B = [[int(x) for x in input().split()] for _ in range(m)]
ans = []
for i in range(n):
    blocks = []
    for j in range(l):
        block = 0
        for k in range(m):
            block += A[i][k]*B[k][j]
        blocks.append(block)
    ans.append(blocks)
for _ in ans:
    print(*_)


n, m, l = map(int, input().split())

A = [[int(s) for s in input().split()] for i in range(n)]
B = [[int(s) for s in input().split()] for i in range(m)]

for x in range(n):
    o = []
    for y in range(l):
        sum = 0
        for z in range(m):
            sum += A[x][z] * B[z][y]
        o.append(str(sum))
    print(" ".join(o))
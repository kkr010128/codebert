A = []
b = []
n, m = map(int,input().split())
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(m):
    b.append(int(input()))

for i in range(n):
    c = 0
    for s in range(m):
        c += A[i][s] * b[s]
    print(c)
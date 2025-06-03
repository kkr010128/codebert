nm = input().split()
n, m = map(int, nm)

A = [[int(i) for i in input().split()] for j in range(n)]

b = [int(input()) for i in range(m)]

for row in A:
    s = 0
    for i, elm in enumerate(row):
        s += (elm*b[i])
    print(s)
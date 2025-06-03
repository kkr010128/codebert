n, m = map(int, raw_input().split())
A = {}
for i in range(n):
    temp = map(int, raw_input().split())
    for j in range(m):
        A[(i,j)] = temp[j]
b = {}
for j in range(m):
    b[(j)] = input()
c = {}
for i in range(n):
    c[(i)] = 0
    for j in range(m):
        c[(i)] += A[(i,j)] * b[(j)]

for i in range(n):
    print c[(i)]
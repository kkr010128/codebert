n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)
for i in range(m):
    bi = int(input())
    b.append(bi)

for i in range(n):
    ci = 0
    for j in range(m):
        ci += a[i][j] * b[j]
    print(ci)
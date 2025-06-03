n, m = map(int, raw_input().split())
a, b, result = list(), list(), list()
for _ in range(n):
    a.append(map(int, raw_input().split()))
for _ in range(m):
    b.append(int(raw_input()))
for i in range(n):
    temp = 0
    for j in range(m):
        temp += a[i][j] * b[j]
    result.append(temp)
for i in result:
    print(i)
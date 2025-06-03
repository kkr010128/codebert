n,m = map(int, input().split())
c = []
d = []
for i in range(n):
    arr = input().split()
    c.append(arr)
for j in range(m):
    d.append(int(input()))
for i in range(n):
    sum = 0
    for j in range(m):
        sum += int(c[i][j])*d[j]
    print(sum)
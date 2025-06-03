r, c = map(int, input().split())
a, b, ans = [], [], []
for i in range(r):
    a.append([int(x) for x in input().split()])
for i in range(c):
    b.append(int(input()))
for i in range(r):
    tmp = 0
    for j in range(c):
        tmp += a[i][j] * b[j]
    ans.append(tmp)
for x in ans:
    print(x)
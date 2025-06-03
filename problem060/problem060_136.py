s = input().split(" ")
n = int(s[0])
m = int(s[1])
l = int(s[2])
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
for i in range(n):
    s = input().split(" ")
    for j in range(m):
        a[i][j] = int(s[j])
for i in range(m):
    s = input().split(" ")
    for j in range(l):
        b[i][j] = int(s[j])
for i in range(n):
    for j in range(l):
        sk = 0
        for k in range(m):
            sk += a[i][k] * b[k][j]
        if j == l-1:
            print(sk)
        else:
            print(sk,end=" ")
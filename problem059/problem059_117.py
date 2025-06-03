s = input().split(" ")
r = int(s[0])
c = int(s[1])
a = [[0 for i in range(c)] for j in range(r+1)]
for i in range(r):
    s = input().split(" ")
    for j in range(c):
        a[i][j] = int(s[j])
for i in range(c):
    sk = 0
    for j in range(r):
        sk += a[j][i]
    a[r][i] = sk
for i in range(r+1):
    sk = 0
    for j in range(c):
        print(a[i][j],end=" ")
        sk += a[i][j]
    print(sk)
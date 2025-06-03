n,m = map(int, raw_input().split())

a = []
b = [0]*m
for i in xrange(n):
    x = map(int,raw_input().split(" "))
    a.append(x)

for i in xrange(m):
    b[i] = input()

result = [0]*n

for i in xrange(n):
    for j in xrange(m):
        result[i] += a[i][j]*b[j]

    print result[i]
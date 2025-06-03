r, c = map(int, input().split())
x = [];
for i in range(r):
    x.append(list(map(int, input().split())))
rsum = [0 for i in range(r)]
csum = [0 for i in range(c)]
total = 0
for i in range(r):
    for j in range(c):
        rsum[i] += x[i][j]
        csum[j] += x[i][j]
        total += x[i][j]
for i in range(r):
    for j in range(c):
        print(str(x[i][j]) + " ", end="")
    print(rsum[i])
for j in range(c):
    print(str(csum[j]) + " ", end="")
print(total)


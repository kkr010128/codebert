n, m = [int(i) for i in input().split()]
vec = []
for i in range(n):
    vec.append([int(j) for j in input().split()])
c = []
for i in range(m):
    c.append(int(input()))
for i in range(n):
    sum = 0
    for j in range(m):
        sum += vec[i][j]*c[j]
    print(sum)
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

l = list(map(int, input().split()))

c = [[0] * (n+1) for i in range(m)]

count = 0
for i in range(1, n+1):
    count += 1
    c[0][i] = count


for i in range(1, m):
    loop = True
    count = 0
    
    for j in range(1, n+1):
        if j - l[i] >= 0:
            if c[i-1][j] > c[i][j-l[i]] + 1:
                c[i][j] = c[i][j-l[i]] + 1
            else:
                c[i][j] = c[i-1][j]
        else:
            c[i][j] = c[i-1][j]


print(c[-1][-1])

n = int(input())
a = []
xy = []

for i in range(n):
    temp_a = int(input())
    s = [list(map(int, input().split())) for _ in range(temp_a)]
    a.append(temp_a)
    xy.append(s)

ans = 0
for bit in range(1<<n):
    h = [0]*n
    flag = True
    sum = 0

    for i in range(n):
        if (bit>>i) & 1:
            h[i] = 1
            sum += 1
                   
    for i in range(n):
        if (bit>>i) & 1:
            for j in range(a[i]):
                if xy[i][j][1] != h[xy[i][j][0]-1]:
                    flag =False

    if flag:
        ans = max((ans, sum))
    
print(ans)



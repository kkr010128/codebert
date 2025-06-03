n,m = (int(i) for i in input().split())
array = [[int(i) for i in input().split()] for i in range(n)]
b = [int(input()) for i in range(m)]
for i in range(n):
    ans = 0
    for i2 in range(m):
        ans += array[i][i2]*b[i2]
    print(ans)
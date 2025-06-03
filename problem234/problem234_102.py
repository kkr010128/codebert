def culc(x):
    a = x % 10
    b = x
    while x:
        b = x
        x //= 10
    return a, b

n = int(input())
l = [[0 for i in range(9)] for j in range(9)]
ans = 0

for i in range(1,n+1):
    a,b = culc(i)
    if a != 0 and b != 0:
        l[a-1][b-1] += 1

for i in range(1,n+1):
    a,b = culc(i)
    if a != 0 and b != 0:
        ans += l[b-1][a-1]
print(ans)
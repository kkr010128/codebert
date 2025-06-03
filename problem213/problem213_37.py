n = int(input())
x = list(map(int, input().split()))
ans = 1000000
for i in range(1, 101):
    s = 0
    for j in range(n):
        s += (x[j] - i)*(x[j] - i)
    ans = min(ans, s)

print(str(ans))

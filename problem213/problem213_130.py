n = int(input())
*x, = map(int, input().split())
ans = float('inf')
for i in range(min(x), max(x)+1):
    tmp = 0
    for j in x:
        tmp += (j - i)*(j - i)
    ans = min(ans, tmp)
print(ans)
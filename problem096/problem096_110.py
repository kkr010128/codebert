n, d = map(int, input().split())
x, y = zip(*[list(map(int, input().split())) for i in range(n)])
 
ans = 0
for i in range(n):
    if x[i]**2 + y[i]**2 <= d**2:
        ans += 1
 
print(ans)
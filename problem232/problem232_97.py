a,b = map(int,input().split())
n = min(a,b)
m = max(a,b)
ans = ''
for i in range(m):
    ans = ans + str(n)
print(ans)
n,m = map(int,input().split())
ans = 0
for i in range(n-1):
    ans = ans + i+1
for b in range(m-1):
    ans = ans + b+1
print(ans)
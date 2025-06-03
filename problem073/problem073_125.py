n = int(input())
ans = 0
for a in range(1, n+1):
    cnt = (n-1)//a
    ans += cnt
print(ans)
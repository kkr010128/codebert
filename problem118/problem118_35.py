from sys import stdin
n = int(stdin.readline())
ans = 0
for j in range(1,n+1):
    a = n//j
    ans += a*(a+1)*j//2
print(ans)
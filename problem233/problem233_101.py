n = int(input())
p = list(map(int,input().split()))
ans = n
m = 2 * (10 ** 5)
for i in range(n):
    m = min(p[i],m)
    if p[i] > m:
        ans -= 1
print(ans)
n = int(input())
ans = 0
for a in range (1,n):
    for b in range(a, n, a):
        ans += 1
print(ans)
n, k = (int(i) for i in input().split())

m = n % k
ans = min(m, k - m)

print(ans)
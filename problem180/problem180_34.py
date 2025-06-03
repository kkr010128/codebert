n, k = [int(i) for i in input().split()]
ans = min((n % k), (k - n % k))
print(ans)
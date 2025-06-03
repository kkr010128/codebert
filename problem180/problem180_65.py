n, k = list(map(int, input().split()))

if n < k:
    ans = min(n, abs(n - k))
else:
    q = n // k
    ans = min(abs(n - (q * k)), abs(n - (q * k) - k))

print(ans)

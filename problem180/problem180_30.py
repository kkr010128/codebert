n, k = map(int, input().split())

if n >= k:
    n %= k
    n = min(n, k-n)
else :
    n = min(n, k-n)

print(n)

n, k = map(int, input().split())

if n == k:
    print(0)
elif n < k:
    print(min(n, k - n))
else:
    n = n % k
    print(min(n, k - n))

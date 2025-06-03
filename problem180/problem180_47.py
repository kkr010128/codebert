n, k = list(map(int, input().split()))
while n > abs(n - k):
    if n >= k:
        n = min(n, n % k)
    elif k > n:
        n = min(n, k % n)
print(n)
n, m = map(int, input().split())
for i in range(1, m+1):
    a, b = i, n-i+1
    if not n % 2 and b-a <= n//2: print(a, b-1)
    else: print(a, b)

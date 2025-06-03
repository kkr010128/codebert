n, a, b = map(int, input().split())

mid = b - a

if mid % 2 == 0:
    print(mid // 2)
else:
    print(min(a - 1, n - b) + 1 + (mid - 1)//2)
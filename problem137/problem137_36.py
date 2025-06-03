n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
a, b = map(list, zip(*ab))
a.sort()
b.sort(reverse=True)
a1, b1 = a[n//2], b[n//2]
a2, b2 = a[n//2-1], b[n//2-1]
if n % 2: print(b1 - a1 + 1)
else: print((b1+b2) - (a1+a2) + 1)

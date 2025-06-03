n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
a.sort()
a = a[::-1]

print('Yes' if s <= 4 * m * a[m - 1] else 'No')

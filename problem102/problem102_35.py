n, k = map(int, input().split())
a = list(map(int, input().split()))

for r in range(k, n, 1):
    l = r - k
    print('Yes' if a[l] < a[r] else 'No')

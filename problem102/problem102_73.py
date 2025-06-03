n, k = map(int, input().split())
*a, = map(int, input().split())
for i, j in zip(a, a[k:]):
    print('Yes' if i < j else 'No')
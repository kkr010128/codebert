n, k = map(int, input().split())
a = list(map(int, input().split()))

for i, j in zip(a[:n-k], a[k:]):
    if i < j:
        print('Yes')
    else:
        print('No')

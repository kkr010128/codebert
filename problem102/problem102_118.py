n, k = map(int, input().split())
a = [int(s) for s in input().split()]

for i in range(k, n):
    if a[i] > a[i - k]:
        print('Yes')
    else:
        print('No') 
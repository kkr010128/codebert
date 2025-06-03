k,n = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

c = a[0] + (k - a[n - 1])

d = max([a[i] - a[i - 1] for i in range(1, n)])

c = max(c,d)

print(k - c)

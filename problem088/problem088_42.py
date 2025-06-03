n = int(input())
a = list(map(int, input().split()))
s = 0

for i in range(0, n - 1):
    h = a[i] - a[i+1]
    if h > 0:
        s += h
        a[i+1] += h
        # a[i+1] = a[i]

print(str(s))

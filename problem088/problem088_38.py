n = int(input())
a = list(map(int, input().split()))
h = 0
for i in range(1, len(a)):
    if a[i-1] > a[i]:
        h += a[i-1] - a[i]
        a[i] += a[i - 1] - a[i]
print(h)
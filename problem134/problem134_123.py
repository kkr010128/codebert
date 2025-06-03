n = int(input())
a = list(map(int, input().split()))
i = 1
if 0 in a:
    i = 0
else:
    for j in range(n):
        if i >= 0:
            i = i * a[j]
        if i > 10 ** 18:
            i = -1
print(int(i))
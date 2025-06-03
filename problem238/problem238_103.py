n, k, s = map(int,input().split())
x = s + 1 if s < 10 ** 9 else 1
a = [x] * n
for i in range(k):
    a[i] = s
print(*a, sep=' ')
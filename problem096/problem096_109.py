a = input().split()
n, d = int(a[0]), int(a[1])
x = []
a = d * d
res = 0
for i in range(n):
    [x, y] = input().split()
    if int(x)**2 + int(y)**2 <= a:
        res += 1
print(res)

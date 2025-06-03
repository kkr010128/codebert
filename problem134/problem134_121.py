n = int(input())
a = list(map(int, input().split()))
x = 1
if 0 in a:
    x = 0
else:
    for i in range(n):
        if x != -1:
            x = x * a[i]
        if x > 10 ** 18:
            x = -1
print(x)
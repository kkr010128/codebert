n = int(input())
a = list(map(int, input().split()))
m = 1
if 0 in a:
    print(0)
else:
    for i in range(n):
        m = m * a[i]
        if m > 10 ** 18:
            print(-1)
            break
        elif i == n - 1:
            print(m)
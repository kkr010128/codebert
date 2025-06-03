n , d = map(int, input().split())
x = []
y = []
for i  in range(n):
        a = list(map(int, (input().split())))
        x.append(a[0])
        y.append(a[1])

ans = 0
for i in  range(n):
        if (x[i] ** 2 + y[i] ** 2) ** (0.5)  <= d:
                ans += 1

print(ans)
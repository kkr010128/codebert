A, B, M = [int(a) for a in input().split()]
a = [int(ai) for ai in input().split()]
b = [int(bi) for bi in input().split()]
x = []
y = []
c = []
for _ in range(M):
    xi, yi, ci = [int(xyc) for xyc in input().split()]
    x.append(xi)
    y.append(yi)
    c.append(ci)

min_price = min(a) + min(b)
for i in range(M):
    price = a[x[i]-1] + b[y[i]-1] - c[i]
    min_price = min(min_price, price)

print(min_price)
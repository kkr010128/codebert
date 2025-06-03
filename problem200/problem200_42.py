A, B, M = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
x = []
y = []
c = []
for _ in range(M):
    xt, yt, ct = [int(x) for x in input().split()]
    x.append(xt)
    y.append(yt)
    c.append(ct)

# 割引券を使わない場合の最小値
ret = min(a) + min(b)

# 割引券を使った場合
for i in range(len(x)):
    t = a[x[i] - 1] + b[y[i] - 1] - c[i]
    if ret > t:
        ret = t

print(ret)
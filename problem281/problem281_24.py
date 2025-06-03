# https://atcoder.jp/contests/abc145/tasks/abc145_d


X, Y = map(int, input().split())

if (2*Y- X) % 3 or (2*X- Y) % 3:
    print(0)
    exit()

x = (2*Y - X) // 3
y = (2*X - Y) // 3

if x < 0 or y < 0:
    print(0)
    exit()

n = x + y
r = x


mod = 10**9 + 7
f = 1
for i in range(1, n + 1):
    f = f*i % mod
fac = f
f = pow(f, mod-2, mod)
facinv = [f]
for i in range(n, 0, -1):
    f = f*i % mod
    facinv.append(f)
facinv.append(1)

print(fac * facinv[r] * facinv[n - r] % mod)
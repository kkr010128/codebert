n = int(input())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
ds = [abs(x - y) for x, y in zip(xs, ys)]
for i in range(1, 4):
    ans = 0
    for d in ds:
        ans += d**i
    print(ans**(1/i))
print(max(ds))

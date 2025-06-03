n = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))

c = [abs(a[i] - b[i]) for i in range(n)]

for p in range(1, 4):
    ans = 0
    for d in c:
        ans += d ** p
    print("{:.6f}".format(ans ** (1 / p)))

print("{:.6f}".format(max(c)))

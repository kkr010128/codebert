n, k = map(int, input().split())
mo = 10 ** 9 + 7
ans = 0
def calc(t):
    u = (0 + t - 1) * t // 2
    v = (n + n - t + 1) * t // 2
    return v - u + 1
for i in range(k, n + 2):
    ans = (ans + calc(i)) % mo
print(ans)
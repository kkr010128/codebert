MOD = 1e9 + 7
n = int(input())
ans = [[0, 1, 1, 8]]
for i in range(n-1):
    a, b, c, d = ans.pop()
    a = (a * 10 + b + c) % MOD
    b = (b * 9 + d) % MOD
    c = (c * 9 + d) % MOD
    d = (d * 8) % MOD
    ans.append([a, b, c, d])

a, b, c, d = ans.pop()
print(int(a))
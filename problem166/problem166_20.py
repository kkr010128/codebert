s = input()
n = len(s)
m = 2019
a = [0] * (n + 1)
b = [0] * (n + 1)
b[0] = 1
for i in range(1, n + 1):
    b[i] = b[i - 1] * 10 % m
c = [0] * m
c[0] += 1
ans = 0
for i in range(n - 1, -1, -1):
    w = (a[i + 1] + (ord(s[i]) - ord('0')) * b[n - 1 - i]) % m
    ans += c[w]
    c[w] += 1
    a[i] = w
print(ans)
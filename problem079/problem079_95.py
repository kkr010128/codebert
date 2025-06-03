import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

s = int(input())

x = s // 3
ans = 0
for xi in range(1, x+1):
    tmp = s - xi*3
    ans += comb(tmp+xi-1, xi-1)
    ans %= 1000000007
print(ans)

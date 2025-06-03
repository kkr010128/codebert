n = int(input())
mod = 10 ** 9 + 7

s = 10 ** n
s0 = 9 ** n
s9 = 9 ** n
sb = 8 ** n

ans = s - s0 - s9 + sb
print(ans % mod)

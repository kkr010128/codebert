x = int(input())
q = x // 100
r = x % 100
r -= 5 * q
print(1 if r <= 0 else 0)

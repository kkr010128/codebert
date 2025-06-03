base, rate = 100, 1.05
for _ in range(int(input())):
    base *= rate
    if not base.is_integer():
        base = int(base) + 1

print(base * 1000)
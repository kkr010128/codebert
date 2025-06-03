base, rate = 100, 0.05
for _ in range(int(input())):
    increment = base * rate
    base += round(increment + (0 if increment.is_integer() else 0.5))

print(base * 1000)
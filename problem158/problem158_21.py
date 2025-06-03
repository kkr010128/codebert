k, a, b = map(int, open(0).read().split())
print("OK" if b // k * k >= a else "NG")
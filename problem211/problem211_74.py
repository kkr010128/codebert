n, r = [int(_) for _ in input().split()]
print(r if n >= 10 else r + 100 * (10 - n))

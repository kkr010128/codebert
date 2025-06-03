m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
print(1 if m2 == m1 % 12 + 1 and d2 == 1 else 0)
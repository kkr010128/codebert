L, R, d = map(int, input().split())
print(R // d - L // d + (L % d == 0))

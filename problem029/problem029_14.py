x, y, p, q = map(float, input().split())
ans = ((p-x)**2 + (q-y)**2)**0.5
print(f"{ans:.8f}")

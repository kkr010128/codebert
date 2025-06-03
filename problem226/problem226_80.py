h, n = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
  h -= a
print("Yes" if h <= 0 else "No")
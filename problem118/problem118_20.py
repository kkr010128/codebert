n = int(input())

ans = 0

for b in range(1, n+1):
  y = n // b
  ans += y*(y+1)*b/2

print(int(ans))
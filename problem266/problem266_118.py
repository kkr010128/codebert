X = int(input())

for c in range(1, 1000001):
  if c * 100 <= X and X <= c * 105:
    ans = 1
    break
  else:
    ans = 0

print(ans)

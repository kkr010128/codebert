n = input()

min_val = float("inf")
max_val = -float("inf")
for i in range(n):
  tmp = input()
  max_val = max(max_val, tmp - min_val)
  min_val = min(min_val, tmp)

print max_val
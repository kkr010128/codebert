n = int(input())
count = 0
for a in range(1, n+1):
  for b in range(1, n+1):
    if a * b < n: count += 1
    else: break
print(count)
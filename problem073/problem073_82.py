n = int(input())
count = 0
for a in range(1, n+1):
  for b in range(a, n+1):
    if n > a * b:
      if a == b: count += 1
      else: count += 2
    else: break
print(count)
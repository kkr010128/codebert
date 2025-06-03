L, R, d = map(int, input().split())
count = 0

for l in list(range(L, R + 1)):
  if l % d == 0:
    count += 1

print(count)

N = int(input())
total = 0
for num in range(1, N+1):
  if num % 15 == 0:
    continue
  if num % 3 == 0 or num % 5 == 0:
    continue
  total += num
print(total)
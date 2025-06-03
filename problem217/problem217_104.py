N = int(input())
A = list(map(int, input().split()))

count = 0
for item in A:
  if item % 2 == 0:
    if item % 3 == 0 or item % 5 == 0:
      count += 1
  else:
    count += 1

if count == N:
  print("APPROVED")
else:
  print("DENIED")
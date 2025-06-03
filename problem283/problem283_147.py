n = int(input())

count = 0

if n < 2:
  print(0)
  exit()
  
for i in range(n//2):
  a = i + 1
  b = n - a
  if a != b and a > 0 and b > 0:
    count = count + 1

print(count)

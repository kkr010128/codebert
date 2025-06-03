n = int(input())

if n < 10:
  print("Yes")
  exit(0)
  
for i in range(2, 10):
  if n % i != 0:
    continue
  v = n // i
  if v < 10:
    print("Yes")
    exit(0)
    
print("No")
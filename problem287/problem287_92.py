n = int(input())
for i in range(9, 0, -1):
  if n % i == 0 and n // i <= 9:
    print('Yes')
    exit()
print('No')
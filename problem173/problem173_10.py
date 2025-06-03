N = int(input())
total = 0
for n in range(1, N+1):
  if (n % 3 > 0) and (n % 5 > 0):
#    print(n)
    total += n
print(total)
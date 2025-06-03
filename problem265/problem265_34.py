n = int(input())
for a in range(1,50001):
  if int(a*1.08) == n:
    print(a)
    exit()
print(':(')
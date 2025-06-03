a = list(map(int, input().split()))

for i in range(10):
  if a.count(i) == 2:
    print('Yes')
    exit()
print('No')

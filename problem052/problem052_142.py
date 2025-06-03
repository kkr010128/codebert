n = [int(x) for x in input().split()]

for nn in range(1, n[0] + 1):
  if nn % 3 == 0 or '3' in str(nn):
    print(' ' + str(nn), end = '')
print()
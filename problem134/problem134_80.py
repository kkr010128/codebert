import sys

n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

multi = 1

if 0 in a:
  print('0')
  sys.exit()

for i in a:
  multi *= i
  if multi > 10**18:
    print('-1')
    sys.exit()

print(multi)
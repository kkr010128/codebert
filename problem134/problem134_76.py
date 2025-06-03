N = int(input())
AS = [int(i) for i in input().split()]

m = 10 ** 18
acc = 1
if 0 in AS:
  print(0)
  import sys
  sys.exit()

for i in AS:
  acc *= i
  if acc > m:
    print('-1')
    import sys
    sys.exit()

print(acc)

def threeDivCheck(x):
  if x % 3 == 0: return x
  return 0

def threeIncludeCheck(x):
  y = x
  while y!=0:
    if y%10 == 3:
      return x
    y=int(y/10)
  return 0

def main():
  n = int(input())
  p = 0
  for i in range(n+1):
    p = threeDivCheck(i)
    if p:
      print(' {}'.format(p), end='')
    else:
      p=threeIncludeCheck(i)
      if p:
        print(' {}'.format(p), end='')
  print()

main()
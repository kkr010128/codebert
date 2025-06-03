ABC = list(map(int,input().split()))
red = ABC[0]
green = ABC[1]
blue = ABC[2]
K = int(input())

for i in range(K):
  if green <= red:
    green *= 2
    continue
  elif blue <= green:
    blue *= 2

if green > red and blue > green:
  print('Yes')
else:
  print('No')
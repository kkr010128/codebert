import math
while True :
  n = int(input())
  if n==0:
    break;
  i = list(map(int, input().split(' ')))
  avg = sum(i)/n
  j = list(map(lambda x: (x-avg)**2, i))
  print("{:.5f}".format(math.sqrt(sum(j)/n)))
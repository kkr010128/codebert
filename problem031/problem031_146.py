from math import sqrt
while True:
  n = int(input())
  if n == 0:
    break
  scores = list(map(int, input().split()))
  ave = sum(scores)/len(scores)
  A = 0
  for i in range(len(scores)):
    A += (scores[i] - ave)**2
  a = sqrt(A/len(scores))
  print('{:.08f}'.format(a))

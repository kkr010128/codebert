import math

A, B = list(map(lambda x : int(x), input().split(" ")))

minPA = A * 12.5
maxPA = (A + 1) * 12.5
minPB = B * 10
maxPB = (B + 1) * 10

if max([maxPA, maxPB]) - min([minPA, minPB]) >= 22.5:
  print(-1)
else:
  m = max([minPA, minPB])
  M = min([maxPA, maxPB])
  if M - m >= M - int(M):
    print(math.ceil(m))
  else:
    print(-1)

import math

prime = [2]
for i in range(3, int(math.sqrt(200000)), 2):
  for j in prime:
    if i % j == 0:
      break
    elif math.sqrt(i) < j:
      prime.append(i)
      break

X = int(input())
if X % 2 == 0 and X != 2:
  X += 1

cand = 0
while not cand:
  for p in prime:
    if X != 2 and X % p == 0:
      break
    elif math.sqrt(X) < p:
      cand = X
      break
  X += 2

print(cand)
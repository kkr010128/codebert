S = input()
import math
half = int(math.ceil(len(S)//2))
count = 0
for a,b in zip(S[:half], S[:-half-1:-1]):
  if a != b: count += 1
print(count)


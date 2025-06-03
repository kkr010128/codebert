from math import gcd
from collections import defaultdict

n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

MOD = 1000000007

box = defaultdict(int)
zeros = 0
for a, b in AB:
  if a == b == 0:
    zeros += 1
  else:
    if a != 0 and b == 0:
      box[(-1, 1, 0)] += 1
    elif a == 0 and b != 0:
      box[(1, 0, 1)] += 1
    else:
      g = gcd(a, b)
      ga = a // g
      gb = b // g
      if (a // b) < 0:
        s = -1
      else:
        s = 1
      box[(s, abs(ga), abs(gb))] += 1
   
nakawaru = dict()
others = 0

for (s, i, j), v in box.items():
    if (-s, j, i) in box.keys():
        if (s, i, j) not in nakawaru.keys() and (-s, j, i) not in nakawaru.keys():    
            nakawaru[(s, i, j)] = (box[(s, i, j)], box[(-s, j, i)])
    else:
        others += v

seed = 1
for i, j in nakawaru.values():
    seed *= (pow(2, i, MOD) + pow(2, j, MOD) - 1)
    seed %= MOD

ans = zeros + pow(2, others, MOD) * seed - 1
ans %= MOD

print(ans)

from math import gcd
mod_val = 1000000007
def simplify(A, B):
  a = A//gcd(A,B)
  b = B//gcd(A,B)
  if b<0:
    return (-a, -b)
  return (a, b)
n = int(input())
count_simple_fish = dict()
bad_fish = 0
for _ in range(n):
  A, B = map(int, input().split())
  if A == B == 0:
    bad_fish = (bad_fish + 1)%mod_val
    continue
  if B == 0:
    if (1, 0) in count_simple_fish:
      count_simple_fish[(1, 0)][1] += 1
    else:
      count_simple_fish[(1, 0)] = [0, 1]
  elif A == 0:
    if (1, 0) in count_simple_fish:
      count_simple_fish[(1, 0)][0] += 1
    else:
      count_simple_fish[(1, 0)] = [1, 0]
  else:
    a, b = simplify(A, B)
    if a>0:
      if (a, b) in count_simple_fish:
        count_simple_fish[(a, b)][1] += 1
      else:
        count_simple_fish[(a, b)] = [0, 1]
    else:
      if (b, -a) in count_simple_fish:
        count_simple_fish[(b, -a)][0] += 1
      else:
        count_simple_fish[(b, -a)] = [1, 0]
big_total = 1
for simple_fish, count_leftright in count_simple_fish.items():
  group_pair_combos = 1
  group_pair_combos = (group_pair_combos + pow(2, count_leftright[1], mod_val) - 1)%mod_val
  group_pair_combos = (group_pair_combos + pow(2, count_leftright[0], mod_val) - 1)%mod_val
  big_total = (big_total * group_pair_combos)%mod_val
big_total = (big_total + bad_fish - 1)%mod_val
print(big_total)
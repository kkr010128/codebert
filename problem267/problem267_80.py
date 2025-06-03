from itertools import product

N = int(input())
S = input()
pins = list(product([i for i in range(10)], repeat=3))
ans = 0
for pin in pins:
  i = 0
  for s in S:
    if pin[i] == int(s):
      i += 1
    if i == 3:
      ans += 1
      break
print(ans)
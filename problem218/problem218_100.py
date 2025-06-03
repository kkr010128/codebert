N = int(input())
BOX = {}

for i in range(N):
  S = input()
  if S in BOX:
    BOX[S] = (BOX[S] + 1)
  else:
    BOX[S] = 0

MAX = max(BOX.values())
keys = [k for k, v in BOX.items() if v == MAX]
keys = sorted(keys)
for i in range(len(keys)):
  print(keys[i])

import sys
readline = sys.stdin.readline

X = int(readline())

limit = 600
rank = 8
for i in range(8):
  if X < limit:
    print(rank)
    break
  limit += 200
  rank -= 1
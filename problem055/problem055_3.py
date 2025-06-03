n = int(input())
record = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
for i in  range(n):
  b, f, r, v = [int(x) for x in input().split()]
  record[b-1][f-1][r-1] += v
for b in range(4):
  for f in record[b]:
    print(' '+' '.join([str(x) for x in f]))
  if b != 3:
    print(''.join(['#' for x in range(20)]))
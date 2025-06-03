F = [[[0] * 10 for i in range(3)] for i in range(4)]
n = int(input())
for i in range(n):
 b, f, r, v = map(int, input().split())
 F[b-1][f-1][r-1] += v
for x in range(0, 4):
 for y in range(0, 3):
  for z in range(0, 10):
   print(" {0}".format(F[x][y][z]), end = '')
  print()
 if x != 3:
  print("#" * 20)
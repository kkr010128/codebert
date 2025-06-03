from sys import stdin
import math
N = int(stdin.readline().rstrip())

for i in range(1, 50000):
  if math.floor(i * 1.08) == N:
    print(i)
    exit()
print(":(")

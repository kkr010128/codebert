import math
import itertools

n = int(input())
data = []

for i in range(n):
  x, y = map(int,input().split())
  data.append((x, y))

cnt = 0

for a in itertools.permutations(range(n)):
  for j in range(n-1):
    cnt += ((data[a[j+1]][0]-data[a[j]][0])**2 + (data[a[j+1]][1]-data[a[j]][1])**2)**0.5

print(cnt / math.factorial(n))
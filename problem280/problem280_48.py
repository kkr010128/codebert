import math
import itertools

n = int(input())
l = []
for _ in range(n):
  a = list(map(int,input().split()))
  l.append(a)

dis = 0
for case in itertools.permutations(l):
  for i in range(n-1):
    dis += math.sqrt((case[i][0]-case[i+1][0])**2+(case[i][1]-case[i+1][1])**2)

result = dis/math.factorial(n)

print(result)
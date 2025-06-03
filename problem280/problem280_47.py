import itertools
import math

n = int(input())
x = []
num = []
for i in range(n):
  x.append([int(t) for t in input().split()])
  num.append(i)

s = 0
for i in itertools.permutations(num):
  i = list(i)
  #print(x,i)
  for j in range(n-1):
    s += math.sqrt((x[i[j]][0] - x[i[j+1]][0])**2 + (x[i[j]][1] - x[i[j+1]][1])**2)
    #print(s)
s /= math.factorial(n)
print(s)
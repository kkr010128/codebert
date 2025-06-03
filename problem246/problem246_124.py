import math
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
import itertools

t=[i for i in range(1,n+1)]
a = list(itertools.permutations(t))




def num(b,t,n):
  c = 0
  for i in range(len(t)):
    if list(t[i]) != b:
      c += 1
    else:
      break
  return(c)


 
x = num(p,a,n)
y = num(q,a,n)
print(abs(x-y))
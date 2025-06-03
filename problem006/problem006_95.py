import math

def myceil(x,n):
  return math.pow(10,-n)*math.ceil(x*math.pow(10,n))

def debt(principal,w):
  if w==1:
    return int(myceil(principal*1.05,-3))
  else:
    return int(debt(myceil(principal*1.05,-3),w-1))



w=int(input())
print(debt(100000,w))
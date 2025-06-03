import math
def order(N,P):
  value=0
  N_ls=list(range(1,N+1))
  score=0
  for i in P:
    score+=N_ls.index(i)*math.factorial(len(N_ls)-1)
    N_ls.remove(i)
  return score

N=int(input())
P=[int(x) for x in input().split()]
Q=[int(x) for x in input().split()]
print(abs(order(N,P)-order(N,Q)))
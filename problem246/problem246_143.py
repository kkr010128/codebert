from math import factorial

N = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]

orderP = 1 + (P[0]-1)*factorial(N-1)
orderQ = 1 + (Q[0]-1)*factorial(N-1)
for i in range(1,N):
  redP = 0
  redQ = 0
  for j in range(i):
    if P[j] < P[i]: redP += 1
    if Q[j] < Q[i]: redQ += 1
  orderP += (P[i]-redP-1)*factorial(N-i-1)
  orderQ += (Q[i]-redQ-1)*factorial(N-i-1)
print(abs(orderP - orderQ))
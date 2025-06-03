from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C_A = Counter(A)
S = 0
for ca in C_A:
  S += ca * C_A[ca]

Q = int(input())
for q in range(Q):
  b, c = map(int,input().split())
  S += (c - b) * C_A[b]
  C_A[c] += C_A[b]
  C_A[b] = 0
  
  print(S)


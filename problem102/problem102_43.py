from collections import deque

N,K = map(int,input().split())

A = [int(i) for i in input().split()]

B = deque(A[:K])

for i in range(K,N):
  if B.popleft() < A[i]:
    print('Yes')
  else:
    print('No')    
    
  B.append(A[i])

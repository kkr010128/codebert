S = input()
N = len(S)
A = [-1 for i in range(N+1)]
if S[0] == "<":
  A[0] = 0
if S[-1] == ">":
  A[-1] = 0
  
for i in range(N):
  if S[i:i+2] == "><":
    A[i+1] = 0

#print(A)

for i in range(N):
  if S[i] == "<":
    A[i+1] = max(A[i]+1, A[i+1])
    
for i in range(N):
  if S[N-i-1] == ">":
    A[N-i-1] = max(A[N-i]+1, A[N-i-1])
    
#print(A)
print(sum(A))
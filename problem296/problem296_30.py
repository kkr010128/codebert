S = list(input())
N = len(S)
K = int(input())
  
if len(set(S)) == 1:
  print((N*K)//2)
  exit()

ans = 0
i = 0
while i < N-1:
  if S[i] == S[i+1]:
    ans += 1
    i += 1
  i += 1

if S[0] != S[N-1]:
  print(ans*K)
  exit()

a = 1
while S[0] == S[a]:
  a += 1

b = 1
while S[N-1] == S[N-1-b]:
  b += 1
print(ans*K - (K-1)*(a//2 + b//2 - (a+b)//2))
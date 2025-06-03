N, K, S = map(int,input().split())
L = [S]*K
for i in range(N-K):
  if S < 10**9:
  	L.append(S+1)
  else:
    L.append(1)
  
print(' '.join(map(str, L)))
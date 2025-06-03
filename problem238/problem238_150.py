N,K,S = map(int,input().split())

if S!=10**9:
  ans = [str(S)]*K + [str(10**9)]*(N-K)
else:
  ans = [str(S)]*K + [str(10**9-1)]*(N-K)
  
print(" ".join(ans))
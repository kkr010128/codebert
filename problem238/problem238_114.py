N , K ,S =map(int,input().split())
if S != 10**9:
  ans = [S]*K  + [10**9]*(N-K)
else:
  ans = [S]*K + [1]*(N-K)
print(" ".join(map(str,ans)))
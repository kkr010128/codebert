N,M = map(int,input().split())
if N > M:
  ans = str(M)*N
else:
  ans = str(N)*M
print(ans)
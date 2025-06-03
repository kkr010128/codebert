N,K = map(int,input().split())
i = N // K
N = N - K * i

ans = N
while True:
  N = abs(N - K)
  if ans > N:
    ans = N
  else:
    break
    
print(ans)
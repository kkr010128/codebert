N, K = (int(x) for x in input().split())
N%=K
dif=N-K
if dif<0:
  dif*=-1
print(min(N, dif))
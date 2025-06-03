import bisect

N, M, K = map(int, input().split())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

sAs = [0]
sBs = [0]
for a in As:
  sAs.append(sAs[-1]+a)
for b in Bs:
  sBs.append(sBs[-1]+b)
  
rlt = 0
for i in range(N+1):
  t = K - sAs[i]
  if t < 0:
    break
  j = bisect.bisect_right(sBs, t)
  rlt = max(rlt, i+j-1)
  
print(rlt)
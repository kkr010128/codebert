N,K = map(int,input().split())
H = list(map(int,input().split()))
H.sort()
reversed(H)
for i in range(K):
  if len(H)==0:
    break
  else:
    H.pop()
if len(H)==0:
  print(0)
else:
  print(sum(H))
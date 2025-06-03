def MI(): return map(int, input().split())
D,T,S=MI()
if D<=T*S:
  print('Yes')
else:
  print('No')
K,S=[input() for i in range(2)]
if len(S)<=int(K):
  print(S)
else:
  print(S[0:int(K)]+"...")
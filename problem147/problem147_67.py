S,T=[input() for i in range(2)]
U=list(S)
W=list(T)
if S in T and len(S)+1==len(T) and U[0]==W[0]:
  print("Yes")
else:
  print("No")
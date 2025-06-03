K,T=[input() for i in range(2)]
A,B=map(int,T.split())
K=int(K)
if (A//K)*K>=A or((A//K)+1)*K<=B:
  print("OK")
else:
  print("NG")
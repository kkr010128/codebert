H1,M1,H2,M2,K = map (int, input ().split ())
S = H1*60+M1
G = H2*60+M2
p = G-S
if p-K < 0:
  print (0)
else:
  print (p-K)
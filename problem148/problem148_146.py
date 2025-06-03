A,B,C,K=map(int,input().split())
if A>=K:
  print(K)
  exit()
elif A+B>=K:
  print(A)
  exit()
else:
  c=K-A-B
  print(A-c)
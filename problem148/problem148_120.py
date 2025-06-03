A,B,C,K = map(int,input().split())

if K-A > 0:
  if K-A-B > 0:
    print(A-(K-A-B))
  else:
    print(A)
else:
  print(K)
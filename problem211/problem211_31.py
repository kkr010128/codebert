A = list(map(int, input().split()))
N=A[0]
R=A[1]
if N>=10:
  print(R)
else:
  print(100*(10-N)+R)
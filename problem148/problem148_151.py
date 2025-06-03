A,B,C,K = map(int,input().split())
count = 0
if K <= A:
  print(K)
elif A < K <= A + B:
  print(A)
elif A +B <= K <= A + B + C:
  x = K -A -B
  print(A -x)
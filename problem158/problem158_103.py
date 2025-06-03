#ABC165-A
K = int(input())
X = list(map(int,input().split()))
if (X[0] // K + 1) * K <=  X[1] or X[0] % K == 0:
  print("OK")
else:
  print("NG")
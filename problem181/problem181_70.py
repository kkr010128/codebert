K = int(input())
A = [i for i in range(1, 10)]
if K <= 9:
  print(A[K-1])
else:
  K -= 9
  f = 1
  while f:
    B = []
    for a in A:
      k = a % 10
      if k != 0:
        B.append(a * 10 + k - 1)
        K -= 1
      if K == 0:
        print(B[-1])
        f = 0
        break
      B.append(a * 10 + k)
      K -= 1
      if K == 0:
        print(B[-1])
        f = 0
        break
      if k != 9:
        B.append(a * 10 + k + 1)
        K -= 1
      if K == 0:
        print(B[-1])
        f = 0
        break
    A = B
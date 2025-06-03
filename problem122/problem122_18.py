from collections import Counter
#N, K = map(int, input().split( ))
#L = list(map(int, input().split( )))
N = int(input())
A = list(map(int, input().split( )))
Q = int(input())
Sum = sum(A)
#Counterなるものがあるらしい
coun = Counter(A)
#Q個の整数の組(B,C)が与えられてB \to Cとして合計を計算
#合計は(Ci-Bi)*(A.count(Bi))変化する.
for _ in range(Q):
  b, c = map(int, input().split( ))
  Sum += (c-b)*coun[b]
  coun[c] += coun[b]
  coun[b] = 0
  print(Sum)
  # replaceするとタイムエラーになるのか…
  #  A = [c if a == b else a for a in A]
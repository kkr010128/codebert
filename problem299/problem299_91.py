N = int(input())
A = list(map(int, input().split()))
idx = [0] * N
for i, val in enumerate(A):
  idx[val-1] = i + 1
for i in idx:
  print(i,end=" ")
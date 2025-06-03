import copy
N = int(input())
A = list(map(int, input().split()))
A_sum = 0
A2 = []
idx = dict()

for i in A:
  if i in idx:
    idx[i] += 1
  else:
    idx[i] = 1
    
for key in idx:
  if idx[key] == 1:
    idx[key] = [idx[key], 0]
  else:
    temp = int(idx[key] * (idx[key] - 1)/2)
    A_sum += temp
    temp = temp - int(temp * (idx[key] - 2) / idx[key])
    idx[key] = [idx[key], temp]
  
for i in range(N):
  key = A[i]
  print(A_sum - idx[key][1])

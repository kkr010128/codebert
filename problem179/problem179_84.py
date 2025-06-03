n,m = list(map(int,input().split()))
A = list(map(int,input().split()))

sum_A = sum(A) / 4 / m
cnt = 0

for i in A:
  if i >= sum_A:
    cnt += 1

if cnt >= m:
  print('Yes')
else:
  print('No')

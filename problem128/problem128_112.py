X, N = map(int, input().split())
if not N ==0:
  A = [int(x) for x in input().split()]
  index = 0
  value = abs(A[0] - X)
  up_list = [0]*(N+1)
  down_list = [0]*(N+1)

  for i in range(N):
    if abs(A[i] - X ) < N+1:
      if A[i] - X >= 0:
        up_list[A[i]-X] = 1
      if A[i] - X <= 0:
        down_list[abs(A[i]- X)] = 1

  j = 0
  while True:
    if down_list[j] == 0:
      print(X-j)
      break
    if up_list[j] ==0:
      print(X+j)
      break
    if j>N+1:
      print('fail')
      break
    j+=1

else:
  print(X)

N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  if A[i] % 2 ==0:
    if A[i] % 3 ==0 or A[i] % 5 ==0:
      pass
      if i == N-1:
        print('APPROVED')
      else:
        pass
    else:
      print('DENIED')
      break
  else:
    if i == N-1:
      print('APPROVED')
    else:
      pass
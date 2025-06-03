N, M = map(int, input().split())
arr = [10] * N
for _ in range(M):
  idx, num = map(int, input().split())
  if arr[idx - 1] == 10:
    arr[idx - 1] = num
  else:
    if arr[idx - 1 ] != num:
      print(-1)
      exit()

if arr[0] == 0:
  if N == 1:
    print(0)
    exit()
  else:
    print(-1)
    exit()
elif arr[0] == 10:
  if N == 1:
    print(0)
    exit()
  else:
    arr[0] = 1
  
for i in range(N):
  if arr[i] == 10:
    arr[i] = 0

for i in arr:
  print(i,end="")

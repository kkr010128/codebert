#D問題
N, K = map(int, input().split())
A = list(map(int, input().split()))

check = [0] * N
time = [-1] * N
check[0] = 1
time[0] = 0
now = 1
t = 1
ex = 0
roop = 0
for i in range(N + 1):
  now = A[now - 1]
  if check[now - 1] == 0:
    check[now - 1] = 1
    time[now - 1] = t
  else:
    ex = time[now - 1]
    roop = t - time[now - 1]
    break
  t += 1
  
if K < t:
  ans = time.index(K) + 1
  print(ans)
else:
  K -= (t - 1)
  K %= roop
  if K == 0:
    K = roop
  #print(K)
  ans = time.index(ex + K - 1) + 1
  print(ans)
  #print(check, time, roop, t, ex)  


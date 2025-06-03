N = int(input())
A = list(map(int,input().split()))
mode = 0
money = 1000
kabu = 0
for i in range(N):
  if i == 0:
    if A[i+1] > A[i]:
      kabu += 1000//A[i]
      money -= kabu*A[i]
      mode = 1
    else:
      continue
  elif i == N-1:
    money += kabu*A[i]
  else:
    if mode == 1:
      if A[i] >= A[i-1]:
        if A[i] > A[i+1]:
          money += kabu*A[i]
          kabu = 0
          mode = 0
        else:
          continue
    else:
      if A[i] < A[i+1]:
        kabu += money//A[i]
        money -= kabu*A[i]
        mode = 1
      else:
        continue
print(money)
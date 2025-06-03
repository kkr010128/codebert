N = int(input())
A_list = list(map(int, input().split()))
zandaka = 1000
kabu = 0
mode = 0

for i in range(N):
  if i == 0:
    if A_list[i + 1] > A_list[i]:
      kabu = 1000 // A_list[i]
      zandaka -= kabu * A_list[i]
      mode = 1
    else:
      continue
  elif i == N - 1:
    zandaka += kabu * A_list[i]
  else:
    if mode == 1:
      if A_list[i] >= A_list[i - 1]:
        if A_list[i] > A_list[i + 1]:
          zandaka += kabu * A_list[i]
          kabu = 0
          mode = 0
        else:
          continue
    else:
      if A_list[i] < A_list[i + 1]:
        kabu = zandaka // A_list[i]
        zandaka -= kabu * A_list[i]
        mode = 1
      else:
        continue

if zandaka >= 1000:
  print(zandaka)
else:
  print(1000)
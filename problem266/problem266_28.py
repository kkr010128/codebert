X = int(input())
N = X // 100
for n in range(N + 1):
  M = X - n * 100
  if M > n * 5:
    continue
  else:
    print(1)
    break
else:
  print(0)
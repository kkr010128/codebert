X = int(input())
K = 1

while K > 0:
  if X * K % 360 == 0:
    print(K)
    break
  else:
    K += 1


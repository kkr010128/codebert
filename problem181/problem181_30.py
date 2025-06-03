K = int(input())
L = [i for i in range(1, 10)]
cnt = 9
i = 0

while K > cnt:
  x = L[i]
  r = x % 10
  if r != 0:
    L.append(10*x + r - 1)
    cnt += 1
  L.append(10*x + r)
  cnt += 1
  if r != 9:
    L.append(10*x + r + 1)
    cnt += 1
  i += 1

print(L[K-1])
X, N = list(map(int, input().split()))

if N == 0:
  print(X)
  exit()

P = list(map(int, input().split()))
up_min = 0
low_min = 0

arr = [0] * 102
for i in P:
  arr[i] = 1
lower = arr[:X]
lower.reverse()
upper = arr[X:]
for i, num in enumerate(lower):
  if num == 0:
    low_min = len(lower) - 1 - i
    break
for i, num in enumerate(upper):
  if num == 0:
    up_min = len(lower) + i
    break

if abs(up_min - X) >= abs(X - low_min):
  print(low_min)
else:
  print(up_min)

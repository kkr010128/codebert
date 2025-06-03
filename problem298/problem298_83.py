N, K = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

def nibu(x, arr):
  if x <= arr[0]:
    return len(arr)
  if arr[-1] < x:
    return 0
  l = 0
  h = len(arr) - 1
  while h - l >1:
    m = (l + h) // 2
    if x <= arr[m]:
      h = m
    else:
      l = m
  return len(arr) - h

print(nibu(K, h))


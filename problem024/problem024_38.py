def check(p, k, arr):
  subtotal = 0
  num_of_tracks = 1
  for a in arr:
    subtotal += a
    if subtotal > p:
      num_of_tracks += 1
      if num_of_tracks > k: return False
      subtotal = a
  return True

n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]

min_p = max(arr)
max_p = sum(arr)
while min_p < max_p:
  mid_p = (min_p + max_p) // 2
  if check(mid_p, k, arr):
    max_p = mid_p
  else:
    min_p = mid_p + 1

print(min_p)
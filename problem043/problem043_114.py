ans = []
while True:
  arr = map(int, raw_input().split())
  if arr[0] == 0 and arr[1] == 0:
    break
  else:
    arr.sort()
    ans.append(arr)

for x in ans:
  print(" ".join(map(str, x)))
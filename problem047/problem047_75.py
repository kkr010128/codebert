ans = []
while True:
  arr = map(str, raw_input().split())
  if arr[1] is '?':
    break

  val = eval(arr[0] + arr[1] + arr[2])
  ans.append(val)

print("\n".join(map(str, ans)))
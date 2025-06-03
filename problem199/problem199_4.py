a = input().strip()
n = len(a)
if(n&1 == 1):
  print("No")
else:
  ans = "Yes"
  for i in range(0, n, 2):
    if(a[i:i+2] != "hi"):
      ans = "No"
  print(ans)
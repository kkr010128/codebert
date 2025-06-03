n = int(input())

res = -1
for x in range(1, n+1):
  if int(x * 1.08) == n:
    res = x

    
if res == -1:
  print(":(")
else:
  print(res)
N = int(input())
a = list(map(int, input().split()))
count = 1
if 0 in a:
  print(0)
else:
  for i in range(N):
    count *= a[i]
    if count > 10 ** 18:
      print(-1)
      break
  else:
    print(count)
a = list(map(int, input().split()))
n = 0
for i in range(5):
  if a[n] == 0:
    print(n+1)
    break
  else:
    n += 1
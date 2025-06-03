n,k = map(int,input().split())
H = sorted(list(map(int,input().split())))
if n <= k:
  print(0)
  exit()
if k == 0:
  print(sum(H))
  exit()
print(sum(H[:-k]))

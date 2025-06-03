h, n = map(int,input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
for v in a:
  h -= v
  if h <= 0:
    print('Yes')
    break
else:
  print('No')
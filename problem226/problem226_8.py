h, n = map(int, input().split())
li = list(map(int, input().split()))

if sum(li) >= h:
  print('Yes')
else:
  print('No')
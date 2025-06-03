h = int(input())
w = int(input())
n = int(input())

if h >= w:
  print(-(-n//h))
elif w > h:
  print(-(-n//w))
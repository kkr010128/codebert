s,w  = map(int,input().split())
if w >= s:
  print("unsafe")
elif w < s:
  print("safe")
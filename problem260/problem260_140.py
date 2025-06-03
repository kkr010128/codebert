a=list(map(int,input().split()))
if sum(a)>=22:
  print("bust")
elif sum(a)<=21:
  print("win")
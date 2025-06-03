num_lis = list(map(int,input().split()))
amount = sum(num_lis)
if amount >= 22:
  print("bust")
else:
  print("win")
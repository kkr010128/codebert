m,d=map(int,input().split())
if m in [1,3,5,7,8,10,12] and d==31:
  print(1)
elif m ==2 and d==28:
  print(1)
elif m in [4,6,9,11] and d==30:
  print(1)
else:
  print(0)
m1,d1 = map(int,input().split())
m2,d2 = map(int,input().split())
if m1 in [1,3,5,7,8,10,12] and d1==31:
  print(1)
elif m1 in [4,6,9,11] and d1==30:
  print(1)
elif m1==2 and d1 in [28,29]:
  print(1)
else:
  print(0)
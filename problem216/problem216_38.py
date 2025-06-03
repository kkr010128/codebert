a,b,c =map(int,input().split())
flag1 = 0
flag2 = 0
flag3 = 0
if a == b:
  flag1 = 1
if b == c:
  flag2 =1
if a == c:
  flag3 =1
if flag1 ==1 and flag2 ==1:
  print("No")
elif flag1 ==0 and flag2 ==0 and flag3 == 0:
  print("No")
else:
  print("Yes")
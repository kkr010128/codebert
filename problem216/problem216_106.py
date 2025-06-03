list1=list(map(int,input().split()))
A=list1[0]
B=list1[1]
C=list1[2]
if list1.count(A)==2 or list1.count(B)==2 or list1.count(C)==2:
  print("Yes")
else:
  print("No")
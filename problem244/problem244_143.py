a=input()
list1=a.split()
list2=list(map(int,list1))
K=list2[0]
X=list2[1]
if 500*K>=X:
  print("Yes")
else:
  print("No")
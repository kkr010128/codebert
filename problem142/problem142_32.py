mylist1 = [2,4,5,7,9]
mylist2 = [0,1,6,8]
N  = int(input())
X = N % 10
if X in mylist1:
  print('hon')
elif X in mylist2:
  print('pon')
else:
  print('bon')
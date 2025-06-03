N = int(input())
A = N%10
B = [2,4,5,7,9]
C = [0,1,6,8]
if A in B:
  print('hon')
elif A in C:
  print('pon')
else:
  print('bon')
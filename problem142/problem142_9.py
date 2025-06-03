N = str(input())

if int(N[-1])==3:
  print('bon')
elif int(N[-1]) in [0, 1, 6, 8]:
  print('pon')
else:
  print('hon')

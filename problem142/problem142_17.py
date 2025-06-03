N = input ()
P = '0168'
H = '24579'
if N[-1] in P:
  print ('pon')
elif N[-1] in H:
  print ('hon')
else:
  print ('bon')
x=list(map(int,input()))
if x[-1]==2 or x[-1]==4 or x[-1]==5 or x[-1]==7 or x[-1]==9:
  print("hon")
elif x[-1]==0 or x[-1]==1 or x[-1]==6 or x[-1]==8:
  print("pon")
else:
  print("bon")
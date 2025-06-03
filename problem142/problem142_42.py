N=str(input())
pon=["0","1","6","8"]
hon=["2","4","5","7","9"]
bon=["3"]

if(N[-1] in pon):
  print("pon")
elif(N[-1] in hon):
  print("hon")
else:
  print("bon")
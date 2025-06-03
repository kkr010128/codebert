a=int(input())
if a%10==3:
  print("bon")
else:
  if a%10==0 or a%10==1 or a%10==6 or a%10==8:
    print("pon")
  else:
    print("hon")
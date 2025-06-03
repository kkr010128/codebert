int = int(input())
dev = int % 10
if dev==3:
  print("bon")
elif dev==0 or dev==1 or dev==6 or dev==8:
  print("pon")
else:
  print("hon")
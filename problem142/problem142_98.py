N = int(input())
N1 = N % 10
if N1 == 3:
  print("bon")
elif (N1 == 0) or (N1 == 1) or (N1 == 6) or (N1 == 8):
  print("pon")
else:
  print("hon")
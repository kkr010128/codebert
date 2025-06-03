n = int(input())
x = n%10
if (x == 2 or x == 4 or x == 5 or x == 7 or x == 9):
  print("hon")
elif (x == 0 or x == 1 or x == 6 or x == 8):
  print("pon")
else:
  print("bon")
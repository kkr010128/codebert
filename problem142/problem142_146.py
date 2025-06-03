N = int(input())
judge = N%10
hon = [2,4,5,7,9]
pon = [0,1,6,8]
bon = [3]
if judge in hon:
  print("hon")
elif judge in pon:
  print("pon")
elif judge in bon:
  print("bon")
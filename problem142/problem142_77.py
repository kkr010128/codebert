n = int(input())

hon = [2, 4, 5, 7, 9]
bon = [3]
pon = [1, 6, 0]
if int(str(n)[-1]) in hon:
  print("hon")
elif int(str(n)[-1]) in bon:
  print("bon")
else:
  print("pon")
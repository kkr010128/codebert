kazu = int(input())
kazu2 = (kazu % 100) % 10
if kazu2 == 3:
  print("bon")
elif kazu2 == 0 or kazu2 == 1 or kazu2 == 6 or kazu2 == 8:
  print("pon")
else:
  print("hon")
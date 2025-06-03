n = int(input())
s = list(str(n))
r = list(reversed(s))

if r[0] in ["2","4","5","7","9"]:
  print("hon")
elif r[0] in ["0","1","6","8"]:
  print("pon")
else:
  print("bon")
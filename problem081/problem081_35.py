text = [int(e) for e in input().split()]

if text[1] * text[2] >= text[0]:
  print("Yes")
else:
  print("No")
H,W = map(int, input().split())
L = []
while H != 0 or W != 0:
 L.append([H, W])
 H,W = map(int, input().split())

def draw(H,W):
 if W == 1:
  for i in range(H // 2):
   print("#")
   print(".")
  if H % 2 == 1:
   print("#")
  print("")
 elif W % 2 == 1:
  for i in range(H // 2):
   print("#." * (W // 2) +"#")
   print(".#" * (W // 2) + ".")
  if H % 2 == 1:
   print("#." * (W // 2) +"#")
  print("")
 else:
  for i in range(H // 2):
   print("#." * (W // 2))
   print(".#" * (W // 2))
  if H % 2 == 1:
   print("#." * (W // 2))
  print("")

for (H, W) in L:
 draw(H,W)
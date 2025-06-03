a, b = map(int, input().split())

aa = ""
for i in range(b):
  aa += str(a)

bb = ""
for i in range(a):
  bb += str(b)  
  
if a <= b :
  print(aa)
else :
  print(bb)
L = []
m, f, r = map(int, input().split())
while not(m == -1 and f == -1 and r == -1):
 L.append([m, f, r])
 m, f, r = map(int, input().split())
 
for i in L:
 if i[0] == -1 or i[1] == -1:
  print("F")
 elif i[0] + i[1] >= 80:
  print("A")
 elif i[0] + i[1] >= 65:
  print("B")
 elif i[0] + i[1] >=  50:
  print("C")
 elif i[0] + i[1] >= 30 and i[2] >=50:
  print("C")
 elif i[0] + i[1] >= 30:
  print("D")
 else:
  print("F")
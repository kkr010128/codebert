a, op, b = input().split()
a = int(a)
b = int(b)
L = []
while op != "?":
 L.append([a, b, op])
 a, op, b = input().split()
 a = int(a)
 b = int(b)

for (a, b, op) in L:
 if op == "+":
  print(str(a + b))
 elif op == "-":
  print(str(a - b))
 elif op == "*":
  print(str(a * b))
 else:
  print(str(a // b))
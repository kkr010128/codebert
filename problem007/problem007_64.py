a = int(input())
f1 = int(2)
f2 = int(1)
f = int(1)
if a == 1:
  print("1")
elif a == 2:
  print("2")
else:
  for b in range(2,a):
    f= f1+f2
    f2 = f1
    f1 = f
  print(f)


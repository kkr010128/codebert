N=int(input())
bandera=False
for i in range(10):
  for j in range(10):
    producto=i*j
    if producto==N:
      bandera=True
if bandera==True:
  print("Yes")
else:
  print("No")
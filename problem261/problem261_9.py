a=input()
l=len(a)
z=0
for i in range(l):
  if a[i]!=a[l-1-i]:
    z+=1
z//=2
print(z)
s=input()
l=len(s)
x=0
for i in range(l):
  x=x+int(s[i])
if x%9==0:
  print("Yes")
else:
  print("No")
s=input()
if len(s)%2!=0:
  print("No")
  exit()
for i,c in enumerate(s):
  if (i%2==0 and c=="h") or (i%2==1 and c=="i"):
    continue
  else:
    print("No")
    exit()
print("Yes")
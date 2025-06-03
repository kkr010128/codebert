s=input()
if len(s)%2==0:
  for i in range(len(s)//2):
    if s[2*i:2*i+2]=="hi":
      continue
    print("No")
    break
  else:
    print("Yes")
else:
  print("No")
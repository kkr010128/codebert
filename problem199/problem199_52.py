S = input()

a = len(S)
if a%2==1:
  print("No")
  exit()
for i in range(0,a,2):
  if S[i:i+2]!="hi":
    print("No")
    break
  else:
    print("Yes")
    break
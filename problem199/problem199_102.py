s=input()
ans=""
if len(s)%2==1:
  print("No")
else:
  n=len(s)//2
  ans="hi"*n
  if ans==s:
    print("Yes")
  else:
    print("No")
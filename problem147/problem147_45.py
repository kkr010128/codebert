s = input()
t = input()
 
flag = True
for i in range(len(s)):
  if s[i] is not t[i]:
    flag = False
if flag is True:
  print("Yes")
else:
  print("No")
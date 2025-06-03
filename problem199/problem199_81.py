s = "hi"
S = input()
flag = False
for i in range(5):
  if S==s:
    flag=True
    break
  s = s+"hi"
if flag:
  print("Yes")
else:
  print("No")
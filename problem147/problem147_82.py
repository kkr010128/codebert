s = input()
t = input()
c = 0 
for i in range(len(s)):
  if s[i]==t[i] and len(t)==len(s)+1:
     c+=1
if c==len(s):
  print("Yes")
else:
  print("No")       
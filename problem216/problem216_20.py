s = input().split()
if s[0]==s[1] and s[0]!=s[2]:
  print("Yes")
elif s[0]==s[2] and s[0]!=s[1]:
  print("Yes")
elif s[2]==s[1] and s[0]!=s[2]:
  print("Yes")
else:
  print("No")
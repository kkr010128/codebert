s =input()
t =input()
for  i in range(len(s)):
  if s[i] != t[i]:
    print('No')
    exit()

if len(t) == len(s)+1:
  print('Yes')
else:
  print('No')
s = input()
t = input()
ans = []
flag = True

for p in range(len(t)):
  ans.append(t[p])
for q in range(len(s)):
  if s[q] != ans[q]:
    flag = False
if flag:
  print('Yes')
else:
  print('No')

def cum(n):
  cum = 0
  for i in range(n+1):
    cum += i
  return cum


s = input()

tmp = s[0]
count = 0
l = []

for each in s:
  if each == tmp:
    count += 1
  else:
    l.append(count)
    count = 1
    tmp = each

l.append(count)

ans = 0
if s[0] == "<":
  for i in range(0,len(l),2):
    tmp = l[i:i+2]
    if len(tmp) == 1:
      ans += cum(tmp[0])
    else:
      ans += cum(max(tmp)) + cum(min(tmp)-1)
else:
  ans += cum(l[0])
  for i in range(1, len(l),2):
    tmp = l[i:i+2]
    if len(tmp) == 1:
      ans += cum(tmp[0])
    else:
      ans += cum(max(tmp)) + cum(min(tmp)-1)

print(ans)
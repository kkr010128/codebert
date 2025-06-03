ans = 0
s = []
for i in range(int(input())):
  a,b = map(int,input().split())
  if a==b:
    ans += 1
    s.append(ans)
  else:
    ans = 0
if len(s)!=0 and max(s)>=3:
  print('Yes')
elif len(s)==0:
  print('No')
else:
  print('No')
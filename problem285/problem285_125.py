s = input()
if s[0] == '>':
  a = [0]
else:
  a = []
flg = 1
for i in range(1,len(s)):
  if s[i] != s[i-1]:
    a.append(flg)
    flg = 1
  else:
    flg += 1
a.append(flg)
if s[-1] == '<':
  a.append(0)
ans = 0
for i in range(len(a)//2):
  if a[2*i] > a[2*i+1]:
    a[2*i+1] -= 1
    ans += a[2*i]*(a[2*i]+1)//2 + a[2*i+1]*(a[2*i+1]+1)//2
  else:
    a[2*i] -= 1
    ans += a[2*i]*(a[2*i]+1)//2 + a[2*i+1]*(a[2*i+1]+1)//2
print(ans)
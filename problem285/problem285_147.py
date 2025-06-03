s = list(input())
l2r = [0]
r2l = [0]
n = len(s)
for i in range(n):
  if s[i] == '<':
    l = l2r[i]
    l2r.append(l+1)
  else:
    l2r.append(0)

for j in range(n):
  if s[n-1-j] == '>':
    r2l.append(r2l[j]+1)
  else:
    r2l.append(0)
invr2l = r2l[::-1]
ans = []
for i in range(n+1):
  m = max(l2r[i],invr2l[i])
  ans.append(m)

print(sum(ans))

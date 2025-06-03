S = str(input())
if len(S) % 2 != 0:
  ans = 'No'
else:
  h = int(len(S) / 2)
  s = [[S[2 * i - 2], S[2 * i -1]] for i in range(h)]
  hi = s.count(['h', 'i'])
  if h == hi:
    ans = 'Yes'
  else:
    ans = 'No'
print(ans)
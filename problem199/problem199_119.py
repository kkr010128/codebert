s = input()
k = len(s)
ans = ''
if k % 2 == 1:
  ans = 'No'
else:
  if s == 'hi' * (k // 2):
    ans = 'Yes'
  else:
    ans = 'No'
print(ans)
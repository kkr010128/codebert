t = input()
ans = list(t)

if ans[-1] == '?':
  ans[-1] = 'D'

tl = len(t)
for i in range(-2, -tl-1, -1):
  if ans[i] == '?':
    if ans[i+1] == 'P':
      ans[i] = 'D'
    else:
      if i != -tl and ans[i-1] == 'P':
        ans[i] = 'D'
      else:
        ans[i] = 'P'
print(''.join(ans))
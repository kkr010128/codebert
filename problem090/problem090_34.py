S = input()
ans = 0
cnt = 0
for w in S:
  if w == 'S':
    ans = max(ans,cnt)
    cnt = 0
  else:
    cnt += 1
ans = max(cnt,ans)
print(ans)
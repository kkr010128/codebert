D = list(input())
ans = 0
cnt = 0

for i in D:
  if i == 'R':
    cnt += 1
  else:
    cnt = 0
  if ans < cnt:
    ans = cnt
print(ans)
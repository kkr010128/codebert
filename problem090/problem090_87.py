s = input()
res = 0
cur = 0
for i in s:
  if i =='S':
    cur = 0
  else:
    cur += 1
  res = max(cur, res)
print(res)
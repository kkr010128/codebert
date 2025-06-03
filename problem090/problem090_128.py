W = list(input())

ans = []
a = 0
for i in W:
  if i == 'R':
    a += 1
  else:
    ans.append(a)
    a = 0

ans.append(a)
print(max(ans))

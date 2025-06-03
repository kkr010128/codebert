s = input()
ans = 0
for i in range(3):
  if s[i] == 'R':
  	ans += 1
  else:
    if ans == 1:
      break
print(ans)
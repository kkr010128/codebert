s = input()
ans = ''
for i in range(len(s)):
  s_i = s[i]
  if s_i == '?':
      ans += 'D'
      continue
  ans += s_i
print(ans)
      

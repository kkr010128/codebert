s = list(input())
ans = 0
for i in range(len(s)):
  if s[i] == '?':
    s[i] = 'D'
print(''.join(s))
s = input()
n = len(s)
if s != s[::-1]:
  print('No')
else:
  s_1 = s[0:(n-1)//2]
  s_2 = s[(n+1)//2:n]
  if s_1 == s_1[::-1] and s_2 == s_2[::-1]:
    print('Yes')
  else:
    print('No')
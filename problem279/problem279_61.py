n = int(input())
s = input()

if n % 2 == 1:
  print('No')
else:
  m = int(n/2)
  s1 = s[: m]
  s2 = s[m: ]
  
  if s1 == s2:
    print('Yes')
  else:
    print('No')

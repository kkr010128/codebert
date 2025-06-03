s = input()

if len(s) % 2 == 1:
  print('No')
else:
  ans = "Yes"
  for i in range(len(s)):
    if i % 2 == 0 and s[i] != 'h':
      ans = "No"
      break
    if i % 2 == 1 and s[i] != 'i':
      ans = "No"
      break

  print(ans)
s = input()

ans = 'Yes'
num = len(s)

if num % 2 != 0:
  ans = 'No'
  pass
else:
  for i in range(0, num, 2):
    if s[i] + s[i+1] != 'hi':
      ans = 'No' 

print(ans)
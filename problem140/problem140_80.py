a = input()
s = list(a)

for i in range(len(s)):
  if (a[i] == '?'):
    s[i] = 'D'

s = "".join(s)
print(s)

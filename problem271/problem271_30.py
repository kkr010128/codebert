n = int(input())
s = input()
x = len(s)
for i in range(x):
  a = s[i]
  b = ord(a)
  c = ord("A")
  d = (b + n - c)%26
  print(chr(c + d), end = '')
print()

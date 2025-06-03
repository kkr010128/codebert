s = input()
l = [0]
m = [0]
a = 0
b = 0
arr = []
for i in range(len(s)):
  if s[i] == '<':
    a += 1
  else:
    a = 0
  l.append(a)

  if s[len(s) - i - 1] == '>':
    b += 1
  else:
    b = 0
  m.append(b)
m = m[::-1]

for i in range(len(l)):
  arr.append(max(l[i], m[i]))
ans = sum(arr)
print(ans)
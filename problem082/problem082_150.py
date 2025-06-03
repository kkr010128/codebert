s = input()
t = input()
l = []
for i in range(len(s)-len(t)+1):
  cha = 0
  for j in range(len(t)):
    if s[j+i] == t[j]:
      cha += 1
  l.append(cha)
print(len(t)-max(l))
s = input()
n = len(s)
c = 0
for i in range(int((n - 1)/2)):
  if (s[i] != s[n - 1 - i]):
    c = 1
x = int((n - 1)/2)
for i in range(x):
  if (s[i] != s[x - 1 - i]):
    c = 1
if (c == 1):
  print("No")
else:
  print("Yes")
  

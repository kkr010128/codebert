n = int(input())
s = str(input())
a = 0
c = len(s)//2
if n % 2 == 0:
  for i in range(c):
    if s[i] == s[c+i]:
      a += 1
  if a == n/2 :
    print("Yes")
  else :
    print("No")
else :
  print("No")
s = input()
n = len(s)
c = 0
for i in range((n+1)//2):
  if s[i] != s[n-i-1]:
    c += 1
print(c)
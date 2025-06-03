s = input()
n = len(s)
n2 = (n+1)//2
for i in range(n):
  if(s[i] != s[n-i-1]):
    print("No")
    exit()
for i in range((n-1)//2):
  if(s[i] != s[n2-2-i]):
    print("No")
    exit()
  if(s[n2+i] != s[n-i-1]):
    print("No")
    exit()
print("Yes")
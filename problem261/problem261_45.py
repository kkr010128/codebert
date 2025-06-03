s = list(input())
n = len(s)-1
count = 0
if s != s[::-1]:
  for i in range(0,(n+1)//2):
    if s[i] != s[n-i]:
      count += 1
print(count)
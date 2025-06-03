s = input()
t = input()
ans = 0
for i in range(len(s)-len(t)+1):
  tm = 0
  for j in range(len(t)):
    if s[i+j] == t[j]:
      tm += 1
  ans = max(tm,ans)
  
print(len(t)-ans)
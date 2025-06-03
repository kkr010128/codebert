n = int(input())
s = input()
cnt = 0

for p in range(len(s)):
  if p <= n - 3:
    if s[p] == 'A':
      if s[p + 1] == 'B' and s[p + 2] == 'C':
        cnt += 1
        
print(cnt)
N = int(input())
s = list(input())
cnt = 0

for i in range(N-2):
  if s[i] == 'A':
    if s[i+1] == 'B':
      if s[i+2] == 'C':
        cnt += 1
        
print(cnt)
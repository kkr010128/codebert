s = input()
cnt = 0

for i in range(len(s)//2):
  if s[i] == s[-i-1]:
    continue
  else:
    cnt += 1
print(cnt)
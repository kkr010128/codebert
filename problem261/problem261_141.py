s=input()
cnt=0
for i in range(len(s)//2):
  cnt += 1 if s[i]!=s[-i-1] else 0
print(cnt)
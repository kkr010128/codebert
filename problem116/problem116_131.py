s = input()
t = input()
cnt = 0
for x in range(len(s)):
    if s[x]!=t[x]:
        cnt+=1
print(cnt)
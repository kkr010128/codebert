s = input()
t = input()
cnt = 0

for i in range(len(s)):
    cnt +=  s[i] != t[i]

print(cnt)
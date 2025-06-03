s = input()
t = input()

cnt = 0

for i in range (len(s)):
    if s[i] == t[i]:
        cnt += 1
if cnt == len(s) and len(t) - len(s) == 1:
    print("Yes")
else:
    print("No")

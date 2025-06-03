n = input()
s = list(n)

sm = 0
for i in range(len(s)):
    sm += int(s[i])
    
if sm%9 == 0:
    print("Yes")
else:
    print("No")

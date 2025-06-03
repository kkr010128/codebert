s = input()
p = input()

flag = False
for i in range(len(s)):
    t = s[i:] + s[:i]
    if p in t :
        flag = True
        break

if flag :
    print("Yes")
else :
    print("No")
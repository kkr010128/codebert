s = input()
p = input()
Flag = False
for i in range(len(s)):
    if len(s)<len(p):
        print("No")
        break
    for j in range(len(p)):
        if i+j>=len(s):
            if s[i+j-len(s)] != p[j]:break
        elif s[i+j] != p[j]:break
        if j == len(p)-1:
            print("Yes")
            Flag = True
            break
    if Flag:break
    if i == len(s)-1:print("No")

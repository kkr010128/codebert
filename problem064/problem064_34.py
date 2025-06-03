s = input()
p = input()
flag = 0
for i in range(len(s)):
    if flag == 1:
        break
    if s[i] == p[0]:
        if len(p) == 1:
            print("Yes")
            flag = 1
            break
        for j in range(1, len(p)):
            i = (i + 1) % len(s)
            if s[i] != p[j]:
                break
            if j == len(p)-1:
                print("Yes")
                flag = 1
                break
if flag == 0:
    print("No")
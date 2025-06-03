s = str(input())
t = str(input())
flag = 0
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        print('No')
        flag = 1
        break
if flag == 0:
    print('Yes')

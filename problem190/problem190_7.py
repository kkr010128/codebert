s = input()
n = len(s)
flag = 1
for i in range(int(n/2)):
    if s[i] != s[n-i-1]:
        flag = 0
        break
n2 = int((n-1)/2)
if flag == 1:
    for i in range(int(n2/2)):
        if s[i] != s[n2-i-1]:
            flag = 0
            break
if flag == 1:
    print("Yes")
else:
    print("No")

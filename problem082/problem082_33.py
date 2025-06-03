s = input()
t = input()
ans = 1001
if len(s)-len(t)==0:
    temp = 0
    for j in range(len(t)):
        if s[j]!=t[j]:
            temp+=1
    ans = min(ans, temp)
else:
    for i in range(len(s)-len(t)):
        temp = 0
        for j in range(len(t)):
            if s[i+j]!=t[j]:
                temp+=1
        ans = min(ans, temp)
print(ans)
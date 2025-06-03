s = str(input())
t = str(input())
ans = 1001
for i in range(len(s)-len(t)+1):
    tmp = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            tmp += 1
    ans = min(len(t)-tmp,ans)
print(ans)
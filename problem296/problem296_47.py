def counter(s):
    cnt = 0
    flag = 0
    for i in range(1, len(s)):
        if flag == 1:
            flag = 0
        else:
            if s[i] == s[i-1]:
                cnt += 1
                flag = 1
    return cnt * k

s = str(input())
k = int(input())
if len(set(s)) == 1:
    ans = len(s) * k // 2
else:
    if k == 1 or s[0] != s[-1]:
        ans = counter(s)
    else:
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == s[0]:
                l += 1
            else:
                break
        for j in range(len(s)-1, 0, -1):
            if s[j] == s[0]:
                r += 1
            else:
                break
        ans = counter(s[l:-r])
        ans += l // 2 + r // 2 + (l + r) // 2 * (k - 1)        
print(ans)

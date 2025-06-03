s = input()
k = int(input())
di = []
cnt = 1
ans = 0
if len(s) > 1:
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            di.append(cnt)
            cnt = 1
    di.append(cnt)
    if di[0] != len(s):
        for j in di:
            ans += j//2
        ans *= k
        if s[0] == s[-1] and di[-1] % 2 == 1 and di[0] % 2 == 1:
            ans += k - 1
    else:
        ans = k*len(s)//2
else:
    ans = k//2
print(ans)
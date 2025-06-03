s = input()
k = int(input())
s_len = len(s)
if s_len == 1:
    print(k//2)
    exit()
if s.count(s[0]) == s_len:
    print((k*s_len)//2)
    exit()
cnt = 0
ans = 0
flag = "off"
while cnt <= s_len-2:
    if s[cnt] == s[cnt+1]:
        if cnt == s_len-2:
            flag = "on"
        ans += 1
        cnt += 1
    cnt += 1
dum = s[0]
check1 = 0
for i in s:
    if dum == i:
        check1 += 1
    else:
        break
dum = s[-1]
check2 = 0
for i in s[::-1]:
    if dum == i:
        check2 += 1
    else:
        break
if (check1+check2)%2 == 0 and s[0] == s[-1]:
    print(ans*k+(k-1))
else:
    print(ans*k)

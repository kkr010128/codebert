s = input()
p = input()
flg = False

for i in range(len(s)):
    s = s[1:] + s[:1]
    if p in s:
        flg = True
        break

if flg:
    print('Yes')
else:
    print('No')
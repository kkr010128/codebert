s = input()
n = len(s)
flg = True
for i in range(n//2):
    if s[i] != s[n-1-i]:
        flg = False
for i in range(n//4):
    if s[i] != s[n//2-1-i]:
        flg = False
print('Yes') if flg else print('No')
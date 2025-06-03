s = list(input())
k = int(input())
s += '+'

releki = []
cnt = 1
pre = s[0]
for i in range(1,len(s)):
    if pre==s[i]:
        cnt += 1
    else:
        releki.append([pre,cnt])
        pre = s[i]
        cnt = 1
        
ans = 0
for i in range(len(releki)):
    ans += releki[i][1]//2
if len(releki)==1:
    print((len(s)-1)*k//2)
    exit()
if s[0]!=s[-3]:
    print(ans*k)
else:
    a = releki[0][1]
    b = releki[-1][1]
    ans = ans*k - (k-1)*(a//2 +b//2 -(a+b)//2)
    print(ans) 


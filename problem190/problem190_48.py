s=input()
n=len(s)
p=n//2
t=1

for i in range(p):
    if s[i]==s[p-1-i]:
        t=1
    else:
        t=0
        break;

x=1

for i in range(p):
    if s[p+1+i]==s[n-1-i]:
        x=1
    else:
       x=0
       break

y=1

for i in range(n):
    if s[i]==s[n-1-i]:
        y=1
    else:
       y=0
       break

if (t==1 and x==1 and y==1):
    print('Yes')
else:
    print('No')
s,k = input(),int(input())
n = len(s)
c = 0
x = []
a = 1
 
for i in range(n):
    if i<n-1 and s[i]==s[i+1]:
        a += 1
    else:
        c += a//2
        x.append(a)
        a = 1
 
c2 = 0
if s[0]==s[-1]:
    c2 = x[0]//2+x[-1]//2-(x[0]+x[-1])//2
 
print(len(s)*k//2 if len(set(s))==1 else c*k-c2*(k-1))
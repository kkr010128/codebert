s = input()
k = int(input())
l=len(s)
s+='?'
ch = 1
ans=0
j=0

for i in range(l):
    if s[i]==s[i+1]:
        ch+=1
    else:
        ans+=ch//2
        if j==0:
            st=ch
        if s[i+1]=='?':
            gl=ch
        ch=1
        j=1
ans*=k
if st%2==1 and gl%2==1 and s[0]==s[l-1]:
    ans+=k-1

if st==l:
    ans=l*k//2

print(ans)

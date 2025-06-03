s=input()
n=int(input())
if len(s)==1:print(n//2);exit()
if len(set(s))==1:print(len(s)*n//2);exit()
c=1
l=[]
for x in range(1,len(s)):
    if s[x-1]==s[x]:
        c+=1
        if x==len(s)-1:l.append(c)
    else:l.append(c);c=1

t=0
if s[0]==s[-1] and l[0]%2==1 and l[-1]%2==1:t=n-1
print(sum([i//2 for i in l])*n+t)
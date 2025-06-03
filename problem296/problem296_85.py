import numpy as np
s=input()
k=int(input())
cnt=1
a=[]
ss=s+"."
for i in range(len(s)):
    if ss[i]==ss[i+1]:
        cnt+=1
    else:
        a.append(cnt)
        cnt=1

pp=0
if s[0]==s[len(s)-1]:
    pp=a[0]+a[-1]
    
    b=[]
    if len(a)>1:
        b.append(pp)
        b+=a[1:len(a)-1]

    else:
        a=[len(s)*k]
        b=[]

else:
    
    b=a
arr=np.array(a)
arr2=np.array(b)

a=arr//2
b=arr2//2
if len(s)>=2:
    print(np.sum(a)+int((k-1)*np.sum(b)))
else:
    print(k//2)
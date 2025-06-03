import math

A=[]
while True:
    n=int(input())
    if n==0:
        break
    s=input().split()
    #m=(s1+s2+...sn)/n
    #H=(s1-m)^2/n+(s2-m)^2/n+...(sn-m)^2/n
    #h=math.sqrt(H)
    i=0
    su=0
    while i<n:
        su+=int(s[i])
        i+=1
    m=su/n

    l=0
    H=0
    while l<n:
        H+=(int(s[l])-m)*(int(s[l])-m)/n
        l+=1
    h=math.sqrt(H)
    A.append(h)

for Ans in A:
    print(Ans)


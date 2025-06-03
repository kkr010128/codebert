import bisect
h,w,k=map(int,input().split())
s=["."*(w+2)]+["."+input()+"." for i in range(h)]+["."*(w+2)]
l=[[0]*(w+2) for i in range(h+2)]
ans=1
for i in range(1,h+1):
    for j in range(1,w+1):
        if s[i][j]=='#':
            l[i][j]=ans
            ans+=1
        
A=1
ss=[]
for i in range(1,h+1):
    if list(set(s[i]))!=['.']:
        ss.append(i)
        for j in range(1,w+1):
            if l[i][j]!=0:
                A=l[i][j]
            elif l[i][j]==0:
                l[i][j]=A
        A+=1
for i in range(1,h+1):
    if i not in ss:
        z=bisect.bisect_left(ss,i)
        if z==len(ss):
            l[i]=l[ss[z-1]]
        else:
            l[i]=l[ss[z]]


for i in range(1,h+1):
    print(" ".join(map(str,l[i][1:-1])))
            


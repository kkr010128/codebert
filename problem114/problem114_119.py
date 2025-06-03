D=int(input())
c=list(map(int,input().split()))
s=[]
for i in range(D):
    s.append(list(map(int,input().split())))

last=[0]*26
ans=0
for d in range(1,D+1):
    t=int(input())
    last[t-1]=d
    temp=0
    for i in range(26):
        if i==t-1:
            temp=s[d-1][t-1]
        else:
            temp=-c[i]*(d-last[i])
        ans+=temp
    print(ans)



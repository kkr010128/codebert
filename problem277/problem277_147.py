h,w,k=map(int,input().split())
s=[]
ans=[[0 for k in range(w)] for _ in range(h)]
for _ in range(h): s.append(input())
temp=0
for i in range(h):
    flag=0
    for j in range(w):
        if flag:
            if s[i][j]=="#": temp+=1
            ans[i][j]=temp
        else:
            if s[i][j]=="#":
                temp+=1
                flag=1
                ans[i][j]=temp
temp=[ans[i].count(0) for i in range(h)]
for i,val in enumerate(temp):
    if 0<val<w:
        j=w-1
        while ans[i][j]!=0: j-=1
        while j>=0:
            ans[i][j]=ans[i][j+1]
            j-=1
for i in range(h):
    if i>0 and ans[i][0]==0: ans[i]=ans[i-1]
for i in range(h-1,-1,-1):
    if i<h-1 and ans[i][0]==0: ans[i]=ans[i+1]
for i in range(h):
    for j in range(w):
        print(ans[i][j],end=" ")
    print()
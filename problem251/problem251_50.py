n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()
a=[]
for i in range(k):
    a.append([])
for i in range(n):
    a[i%k].append(t[i])
for i in range(k):
    for j in range(len(a[i])):
        if j>=1:
            if a[i][j]==a[i][j-1]:
                a[i][j]=0
ans=0
for i in range(k):
    for j in range(len(a[i])):
        if a[i][j]=="r":
            ans+=p
        elif a[i][j]=="s":
            ans+=r
        elif a[i][j]=="p":
            ans+=s
print(ans)
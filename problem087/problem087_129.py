a=list(input())
ans=0
for i in range(len(a)):
    ans+=int(a[i])
if ans%9==0:
    print("Yes")
else:
    print("No")
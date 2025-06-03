n=input()
ans=0
if n=="0":
    print("Yes")
else:
    for i in n:
        ans+=int(i)
    if ans%9==0:
        print("Yes")
    else:
        print("No")
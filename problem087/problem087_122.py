n=input()
ans=0
for i in range(len(n)):
    ans+=int(n[i])
if ans%9:
    print("No")
else:
    print("Yes")
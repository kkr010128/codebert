n=input()
lis=["SUN","MON","TUE","WED","THU","FRI","SAT"]
ans=7
for i in lis:
    if n==i:
        print(ans)
        break
    ans-=1
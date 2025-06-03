s=input()
num=s.count("R")

if num==2:
    if s=="RSR":
        ans=1
    else:
        ans=2
else:
    ans=num

print(ans)
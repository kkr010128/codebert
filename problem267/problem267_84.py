n=int(input())
s=input()

ans=0
for i in range(1000):
    cs=str(i).zfill(3)
    p=0
    for c in cs:
        p=s.find(c,p)

        if p==-1:
            break
        p+=1

    else:
        ans+=1

print(ans)
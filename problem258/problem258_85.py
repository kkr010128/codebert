N=int(input())

if N%2==1:
    print(0)
    exit()
elif N==0:
    print(0)
    exit()

L=len(str(N))
ans=0
now=5
while N//now>0:
    ans+=((N//now)//2)
    now*=5
print(ans)

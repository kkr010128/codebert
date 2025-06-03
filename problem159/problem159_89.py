x=int(input())
n=100
ans=0
while True:
    ans+=1
    n+=n//100
    if n>=x:
        print(ans)
        break
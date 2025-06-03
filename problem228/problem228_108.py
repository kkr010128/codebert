H=int(input())
ans=0
i=0
while 2**i<=H:
    ans+=2**i
    i+=1
print(ans)
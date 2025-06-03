H=int(input())

x=0
while True:
    x+=1
    if 2**x>H:
        x-=1
        break

ans=0
for i in range(x+1):
    ans+=2**i

print(ans)
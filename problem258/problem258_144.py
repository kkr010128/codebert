N=int(input())

ans=0
if ~N%2:
    for i in range(1,30):
        ans+=N//(10*5**i)
    ans+=N//10
print(ans)
N=int(input())

ans=0
if ~N%2:
    for i in range(1,30):
        ans+=N//(2*5**i)
print(ans)
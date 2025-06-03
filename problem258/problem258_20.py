n=int(input())
ans=0
if n%2==0:
    for i in range(1,26):
        ans+=(n//(2*5**i))
print(ans)
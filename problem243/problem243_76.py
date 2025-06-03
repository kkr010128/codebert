N=int(input())
st= [list(map(str, input().split())) for _ in range(N)]
X=input()
ans=0
check=0
for i in range(N):
    if check==1:
        ans+=int(st[i][1])
    if st[i][0]==X:
        check=1
    
print(ans)
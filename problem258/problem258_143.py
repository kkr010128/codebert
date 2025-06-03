N=int(input())

if N%2==1:
    print(0)
    exit(0)

ans=N//10
cur=N//10
while cur//5>0:
    cur//=5
    ans+=cur


print(ans)

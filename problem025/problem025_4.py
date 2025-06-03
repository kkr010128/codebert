N=int(input())
A=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
num_list=set()
for i in range(2**N):
    ans=0
    for j in range(N):
        if i>>j&1:
            ans+=A[j]
    num_list.add(ans)
for i in q:
    if i in num_list:
        print("yes")
    else:print("no")


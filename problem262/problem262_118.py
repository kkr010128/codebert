def check(i,N,Ls):
    count=0
    for j in range(N):
        if (i>>j)%2==1:
            for k in Ls[j]:
                if ((i>>(k[0]-1))%2)!=k[1]:
                    return 0
            count+=1
    return count
                
N=int(input())
A_ls=[]
Ls=[]
for i in range(N):
    A=int(input())
    A_ls.append(A)
    ls=[]
    for j in range(A):
        x,y=map(int,input().split())
        ls.append((x,y))
    Ls.append(ls)

ans=0
for i in range(2**N):
    num=check(i,N,Ls)
    if num>ans:
        ans=num
print(ans)
A,B,N=map(int,input().split())
# A,B,N=11, 10, 5

ans=0

if N>=B:
    ans=(A*(B-1))//B - A*((B-1)//B)
else:
    ans=(A*N)//B - A*(N//B)

print(ans)
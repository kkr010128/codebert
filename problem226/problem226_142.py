H,N=map(int,input().split())
A=sorted(list(map(int,input().split())))
for i in range(1,N+1):
    H-=A[-i]
    if H<=0:
        print('Yes')
        exit()
print('No')
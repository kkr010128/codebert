L=list(map(int,input().split()))
L[2],L[0]=L[0],L[2]
L[1],L[2]=L[2],L[1]
print(*L)
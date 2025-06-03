A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
List=[list(map(int,input().split())) for i in range(M)]
minn=min(a)+min(b)

for i in range(M):
    minn=min(minn,a[List[i][0]-1]+b[List[i][1]-1]-List[i][2])

print(minn)
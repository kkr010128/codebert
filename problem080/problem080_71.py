N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]

za,wa=-10**10,-10**10
zi,wi=10**10,10**10
for i in range(N):
    z=arr[i][0]+arr[i][1]
    w=arr[i][0]-arr[i][1]
    
    za=max(z,za)
    zi=min(z,zi)
    
    wa=max(w,wa)
    wi=min(w,wi)

print(max(za-zi,wa-wi))
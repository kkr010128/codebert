N=int(input())
L=list(map(int,input().split()))
cnt=0
for i in range(0,N-2,1):
    for j in range(i+1,N-1,1):
        for k in range(j+1,N,1):
            if L[i]!=L[j] and L[j]!=L[k] and L[k]!=L[i] and L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j]:
                cnt=cnt+1
print(cnt)

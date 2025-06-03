N=int(input())
L=list(map(int, input().split()))
count=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            L2=[L[i],L[j],L[k]]
            L2.sort()
            if L2[0]+L2[1]>L2[2] and L2[0] != L2[1] and L2[1] != L2[2] and L2[2] != L2[0]:
                count+=1
                
print(count)

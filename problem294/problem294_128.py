N=int(input())
L= list(map(int,input().split()))
L_sorted=sorted(L,reverse=False)#昇順
count=0
import bisect
for i in range(N):
    for j in range(i+1,N):
        a=L_sorted[i]
        b=L_sorted[j]        
        bisect.bisect_left(L_sorted,a+b)
        count+=bisect.bisect_left(L_sorted,a+b)-j-1
print(count)
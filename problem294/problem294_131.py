from bisect import bisect_left
N=int(input())
A=sorted(list(map(int,input().split())))
cnt=0
for i in range(N-1):
    for j in range(i+1,N):
        a=bisect_left(A,A[i]+A[j])
        if j<a:
            cnt+=a-j-1
print(cnt)
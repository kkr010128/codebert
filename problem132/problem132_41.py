N,K = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
while cnt<K:
    B = [0 for _ in range(N+1)]
    for i in range(N):
        a = A[i]
        B[max(i-a,0)] += 1
        B[min(i+a,N-1)+1] -= 1
    for i in range(1,N+1):
        B[i] += B[i-1]
    A = B[:N]
    flag = 0
    for i in range(N):
        if A[i]<N:
            flag = 1
            break
    if flag==0:break
    cnt += 1
print(*A)
N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
if N%2==0:
    cnt = A[0]
    for i in range(1,N//2):
        cnt += 2*A[i]
    print(cnt)
else:
    cnt = A[0]
    for i in range(1,N//2):
        cnt += 2*A[i]
    cnt += A[N//2]
    print(cnt)
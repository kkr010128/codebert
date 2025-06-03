N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
A = sorted([X[i][0] for i in range(N)])
B = sorted([X[i][1] for i in range(N)])
if N%2==1:
    a = A[N//2]
    b = B[N//2]
    print(b-a+1)
else:
    a = (A[(N-1)//2]+A[N//2])/2
    b = (B[(N-1)//2]+B[N//2])/2
    print(int((b-a)/0.5)+1)

N = int(input())
A = list(map(int,input().split()))
LEFT = A[0]
RIGHT = sum(A[1:])
MIN = abs(LEFT-RIGHT)
for i in range(1,N-1):
    LEFT += A[i]
    RIGHT -= A[i]
    MIN = min(MIN,abs(LEFT-RIGHT))
print(MIN)
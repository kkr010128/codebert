N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
U = max(A)+1
L = 0


def can(x, K):
    ct = 0
    for i in range(N):
        ct += (A[i]-1)//x
    if ct <= K:
        return True
    else:
        return False


while U-L > 1:
    x = (U+L+1)//2
    if can(x, K):
        U = x
    else:
        L = x

print(U)

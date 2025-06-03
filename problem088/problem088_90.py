N = int(input())
A = list(map(int, input().split()))
cun =0
for i in range(N):
        if i == N-1:
            break
        elif A[i] > A[i+1]:
            cun += A[i] - A[i+1]
            A[i+1] = A[i]
        else:
            pass
print(cun)
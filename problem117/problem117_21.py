N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
b_ind = 0

for x in range(N-1):
    A[x+1] += A[x]
    if A[x+1] > K:
        A = A[:x+1]
        break

for y in range(M-1):
    B[y+1] += B[y]
    if B[y+1] > K:
        B = B[:y+1]
        break

A = [0] + A
B = [0] + B

na = len(A)
nb = len(B) 

if A[-1] + B[-1] <= K:
    answer = len(A) + len(B) - 2
    print(answer)

else:
    for i in range(na):
        for j in range(nb-b_ind-1, -1, -1):
            if A[i] + B[j] <= K:
                if answer < i+j:
                    answer = i+j
                b_ind = nb-j-1
                break
    print(answer)
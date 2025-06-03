N = int(input())
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    a,b = map(int,input().split())
    A[i] = a
    B[i] = b

A_sort = sorted(A)
B_sort = sorted(B)

if N % 2 == 1:
    print(B_sort[N//2] - A_sort[N//2] + 1)
else:
    med_A = (A_sort[N//2] + A_sort[N//2 - 1])
    med_B = (B_sort[N//2] + B_sort[N//2 - 1])
    print(med_B - med_A + 1)
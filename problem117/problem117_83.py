N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_num = 0
j = 0
j_max = M
A_sums=[0]
B_sums=[0]
for i in range(N):
    A_sums.append(A_sums[i]+A[i])
for i in range(M):
    B_sums.append(B_sums[i]+B[i])


for i in range(N + 1):
    j = 0
    if A_sums[i]>K:
        break
    while A_sums[i]+B_sums[j_max] > K:
        j_max -=1

    max_num = max(max_num, i + j_max)
print(max_num)

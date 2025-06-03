N, M, K = list(map(int, input().split()))
A = [0] + [int(i) for i in input().split() ]
B = [0] + [int(i) for i in input().split() ]

best = 0
a_time = 0
b_time = sum(B)
b_i = len(B)-1
end_flag = False
for a_i in range(N+1):
    a_time += A[a_i]
    while a_time + b_time > K:
        if b_i == 0:
            end_flag = True
            break
        b_time -= B[b_i]
        b_i -= 1

    if end_flag == True:
        break
    if a_i + b_i > best:
        best = a_i + b_i

print(best)
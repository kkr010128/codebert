N, M, K = map(int, input().split(' '))
A_ls = [0] + list(map(int, input().split(' ')))
for i in range(len(A_ls) - 1):
    A_ls[i + 1] += A_ls[i]

B_ls = [0] + list(map(int, input().split(' ')))
for i in range(len(B_ls) - 1):
    B_ls[i + 1] += B_ls[i]

b_cnt,result = M, 0
for a_cnt in range(N + 1):
    if A_ls[a_cnt] > K:
        break
    while A_ls[a_cnt] + B_ls[b_cnt] > K:
        b_cnt -= 1
    result = max(result, a_cnt + b_cnt)
print(result)
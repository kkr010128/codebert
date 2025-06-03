A, B, C = map(int, input().split())
K = int(input())
i_ans = 0
j_ans = 0
for i in range(0,8):
    B_after = B * (2 ** i)
    if B_after > A:
        i_ans = i
        break
B_after = B * (2 ** i_ans)
for j in range(0,8):
    C_after = C * (2 ** j)
    if C_after > B_after:
        j_ans = j
        break
if i_ans + j_ans <=K:
    print('Yes')
else:
    print('No')
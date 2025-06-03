N = int(input())
A = list(map(int, input().split()))

ans = 0
if N == 0:
    if A[0] >= 2:
        ans = -1
    else:
        ans = 1

if N >= 1 and A[0] >= 1:
    ans = -1

if N >= 1:
    node_num = {N: A[N]}
    max_parent_num = {0: 1}
    for i in range(1, N+1):
        max_parent_num[i] = max_parent_num[i-1] * 2 - A[i]

    for i in range(N, 0, -1):
        if node_num[i] > A[i] + max_parent_num[i]:
            ans = -1
            break
        #i-1 no parent wo tukuru
        if node_num[i] <= max_parent_num[i-1]:
            i_1_parent_num = node_num[i]
        else:
            i_1_parent_num = max_parent_num[i-1]
        node_num[i-1] = i_1_parent_num + A[i-1]
        if i == 1:
            if node_num[i-1] != 1:
                ans = -1
                break

if ans == -1 or ans == 1:
    print(ans)
else:
    ans = sum(node_num.values())
    print(ans)
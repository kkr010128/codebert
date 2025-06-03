S = input()
K = int(input())

if S[0] != S[-1]:
    ans = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            S = S[:i + 1] + '*' + S[i + 2:]
            ans += 1
    print(ans * K)
else:
    # S -> s_1 s_2 ... s_k + A + t_l t_l-1 ... t_1 (s_i = t_j)と分解
    k, l = 0, len(S) - 1
    while k < len(S) and S[k] == S[-1]:
        k += 1
    while l > -1 and S[l] == S[0]:
        l -= 1

    # 連結に関係ない部分のカウント
    A = S[k:l + 1]
    ans = 0
    for i in range(len(A) - 1):
        if A[i + 1] == A[i]:
            A = A[:i + 1] + '*' + A[i + 2:]
            ans += 1
    ans *= K

    # 連結に関係ある部分のカウント
    if l == -1 and k == len(S):
        # 全部同じ
        print((len(S) * K) // 2)
    else:
        ans += (len(S) - l + k - 1) // 2 * (K - 1)
        ans += (len(S) - l - 1) // 2 + k // 2
        print(ans)

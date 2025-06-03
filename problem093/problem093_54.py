n, k = map(int, input().split())

p = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

p_flag = [0 for _ in range(len(p))]
loop_max = []
loop_len = []
S = []
S_max = []
ans = []

for i in range(len(p)):
    # if p_flag[i] == 1:
    #     continue
    now = i
    temp_len = 0
    temp_s = 0
    S_max = - (10**9 + 1)
    temp_l = []
    while True:
        now = p[now] - 1
        temp_len += 1
        temp_s += c[now]
        temp_l.append(temp_s)
        p_flag[now] = 1

        # 最初に戻ってきたら
        if now == i:
            break

    loop_len.append(temp_len)
    loop_max.append(temp_l)
    S.append(temp_s)

for i in range(len(S)):
    mod = k % loop_len[i] if k % loop_len[i] != 0 else loop_len[i]
    if S[i] > 0:
        if max(loop_max[i][:mod]) > 0:
            ans.append(((k-1)//loop_len[i])*S[i] + max(loop_max[i][:mod]))
        else:
            ans.append(((k - 1) // loop_len[i]) * S[i])
    else:
        ans.append(max(loop_max[i]))

# print(loop_max)
# print(ans)
print(max(ans))

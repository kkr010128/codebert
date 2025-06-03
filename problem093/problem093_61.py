N, K = list(map(int, input().split()))
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

max_score = -1 * float('inf')

for start_pos in range(N):
    step_score = []
    pos = start_pos
    loop_num = 0
    loop_sum = 0
    step = 0
    while (step < K):
        pos = P[pos]
        loop_sum += C[pos]
        step_score.append(loop_sum)
        step += 1
        if pos == start_pos:
            break
    loop_num = step
    step_max_score = max(step_score)
    if loop_num < K:
        if K // loop_num > 0:
            if K % loop_num != 0:
                step_max_score = max(
                    step_max_score,
                    max(step_score[:(K % loop_num)]) + loop_sum * (K // loop_num)
                )
            else:
                step_max_score = max(
                    step_max_score,
                    loop_sum * (K // loop_num)
                )
        if K // loop_num > 1:
            step_max_score = max(
                step_max_score,
                max(step_score) + loop_sum * (K // loop_num - 1)
            )
    max_score = max(step_max_score, max_score)
    #print(start_pos, step_max_score, max(step_score), loop_sum, loop_num)

print(max_score)
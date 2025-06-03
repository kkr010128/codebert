N, K = map(int, input().split())

sum_pattern_num = 0

for num_cnt in range(K, N+2):
    if num_cnt == K:
        min_sum_frac = sum([i for i in range(0, K)])
        max_sum_frac = sum([i for i in range(N - K + 1, N + 1)])
    else:
        min_sum_frac = min_sum_frac + (num_cnt - 1)
        max_sum_frac = max_sum_frac + (N - num_cnt + 1)
    sum_pattern_num = \
        (sum_pattern_num + (max_sum_frac - min_sum_frac + 1)) % 1000000007

print(sum_pattern_num)
n, k = map(int, input().split())
p_list = list(map(lambda x: int(x) - 1, input().split()))
c_list = list(map(int, input().split()))

max_score = -(1 << 64)
cycles = []
cycled = [False] * n
for i in range(n):
    if cycled[i]:
        continue

    cycle = [i]
    cycled[i] = True
    while p_list[cycle[-1]] != cycle[0]:
        cycle.append(p_list[cycle[-1]])
        cycled[cycle[-1]] = True

    cycles.append(cycle)

for cycle in cycles:
    cycle_len = len(cycle)

    accum = [0]
    for i in range(cycle_len * 2):
        accum.append(accum[-1] + c_list[cycle[i % cycle_len]])

    cycle_score = accum[cycle_len]

    max_series_sums = [max([accum[i + length] - accum[i]
                            for i in range(cycle_len)])
                       for length in range(cycle_len + 1)]

    if cycle_len >= k:
        score = max(max_series_sums[1:k + 1])
    elif cycle_score <= 0:
        score = max(max_series_sums[1:])
    else:
        max_cycle_num, cycle_rem = divmod(k, cycle_len)
        score = max(cycle_score * (max_cycle_num - 1) + max(max_series_sums),
                    cycle_score * max_cycle_num + max(max_series_sums[:cycle_rem + 1]))

    max_score = max(max_score, score)

print(max_score)

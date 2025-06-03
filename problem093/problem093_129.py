N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [None] + P
C = [None] + C

all_max = C[1]
for st in range(1, N + 1):
    p = P[st]
    scores = [C[p]]

    while p != st and len(scores) < K:
        p = P[p]
        scores.append(C[p])

    num_elem = len(scores)
    all_sum = sum(scores)

    q, r = divmod(K, num_elem)

    max_ = scores[0]
    temp = scores[0]

    max_r = scores[0]
    temp_r = scores[0]
    for x in range(1, num_elem):
        if x < r:
            temp_r += scores[x]
            max_r = max(max_r, temp_r)

        temp += scores[x]
        max_ = max(max_, temp)

    temp_max = scores[0]
    if all_sum > 0 and q > 0:
        if r > 0:
            temp_max = max(all_sum * (q - 1) + max_, all_sum * q + max_r)
        else:
            temp_max = all_sum * (q - 1) + max_
    else:
        temp_max = max_

    all_max = max(all_max, temp_max)


print(all_max)

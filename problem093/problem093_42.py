N, K = map(int, input().split())
Ps = list(map(int, input().split()))
Ps = [i - 1 for i in Ps]
Cs = list(map(int, input().split()))
max_score = -float("inf")


for i in range(N):
    scores = []
    idx = i  # starting index
    while True:
        idx = Ps[idx]  # point to the next index
        scores.append(Cs[idx])  # fetch a score to add
        if idx == i:  # when the cycle is closed
            break

    len_cycle = len(scores)
    sum_cycle = sum(scores)

    if sum_cycle <= 0:  # when each cycle reduces the total score
        score = 0
        for j in range(min(K, len_cycle)):
            score += scores[j]
            max_score = max(max_score, score)
    else:
        if K // len_cycle > 0:
            num_multiply = K // len_cycle - 1
            score = sum_cycle * num_multiply
            scores = scores * 2
            for j in range(K % len_cycle + len_cycle):
                score += scores[j]
                max_score = max(max_score, score)
        else:
            num_multiply = 0  # len_cycle > K
            score = sum_cycle * num_multiply
            for j in range(K):
                score += scores[j]
                max_score = max(max_score, score)

print(max_score)

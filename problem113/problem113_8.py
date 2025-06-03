# 入力
D = int(input())
C = list(map(int, input().split()))
S_2d = []
for i in range(D):
    s_1d = list(map(int, input().split()))
    S_2d.append(s_1d)
# T = []
# for i in range(D):
#     t = int(input())
#     T.append(t)

last_days = [0] * 26
tot_score = 0

def scoring(day, tot_score, today_contest):
    today_plus = S_2d[day - 1][today_contest]
    today_minus = 0
    for j, c in enumerate(C):
        today_minus += c * (day - last_days[j])
    return (today_plus - today_minus)


for i in range(D):
    best_score = -10**100
    best_contest = 0
    for k, _ in enumerate(C):
        last_days[k] = i + 1
        k_score = scoring(i + 1, tot_score, k)
        if best_score < k_score:
            best_score, best_contest = k_score, k + 1
    tot_score += best_score
    print(best_contest)


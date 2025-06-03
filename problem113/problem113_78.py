import copy
# 入力
D = int(input())
C = list(map(int, input().split()))
S_2d = []
for i in range(D):
    s_1d = list(map(int, input().split()))
    S_2d.append(s_1d)

last_days = [0] * 26
tot_score = 0

def scoring(day, tot_score, today_contest, last_days):
    today_plus = S_2d[day - 1][today_contest]
    today_minus = 0
    for j, c in enumerate(C):
        today_minus += c * (day - last_days[j])
    # print(today_plus, today_minus)
    return (today_plus - today_minus)

# A
for i in range(D):
    best_score = -10**100
    best_contest = 0
    for k, _ in enumerate(C):
        last_days_tmp = copy.copy(last_days)
        last_days_tmp[k] = i + 1
        k_score = scoring(i + 1, tot_score, k, last_days_tmp)
        if best_score < k_score:
            best_score, best_contest = k_score, k
    last_days[best_contest] = i + 1
    tot_score += best_score
    print(best_contest + 1)

# # B
# T = []
# for i in range(D):
#     t = int(input())
#     T.append(t)
# for i in range(D):
#     last_days[T[i] - 1] = i + 1
#     tot_score += scoring(i+1, tot_score, T[i] - 1)
#     print(tot_score)

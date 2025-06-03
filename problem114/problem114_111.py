NUM_CONTESTS = 26

def main():
    D = int(input())
    c_list = list(map(int, input().split()))
    s_list = [list(map(int, input().split())) for _ in range(D)]

    t_list = [int(input()) for _ in range(D)]
    v_list = calc_score_list(s_list, c_list, t_list)

    for v in v_list:
        print(v)


def calc_score_list(s_list, c_list, t_list):
    last = [-1 for _ in range(NUM_CONTESTS)]
    score_list = []
    score = 0
    for d, t in enumerate(t_list):
        last[t - 1] = d
        score += s_list[d][t - 1] - sum([c * (d - l) for c, l in zip(c_list, last)])
        score_list.append(score)
    return score_list



if __name__ == "__main__":
    main()

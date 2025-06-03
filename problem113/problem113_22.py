#計算ミスあり最終スコアがtesterと異なる
import random
import time

def search(day, schedule, c, s, satisfy):
    score = 0
    date = [0] * 26
    for d in range(day):
        tmp = 0
        contest = 0
        nmax = -float('inf')
        for i in range(26):
            tmp += c[i] * (d + 1 - date[i])
        for i in range(26):
            tmp2 = s[d][i] - tmp + c[i] * (d + 1 - date[i])
            if nmax < tmp2:
                nmax = tmp2
                contest = i
        
        date[contest] = d + 1
        satisfy.append(tmp - c[contest] * (d + 1 - date[contest]))
        schedule.append(contest)
        score += s[d][contest] - satisfy[d]

    return score
    
# def decrease(day, schedule, c, s, satisfy):
#     ret = 0
#     date = [0] * 26

#     for d in range(day):
#         now = schedule[d] + 1
#         date[now - 1] = d + 1
#         tmp = 0
#         for i in range(26):
#             tmp += c[i] * (d+1 - date[i])
#         ret += tmp
#         satisfy.append(tmp)

#     return ret

def change(_from, _to, schedule, c, s, satisfy):
    ret = 0
    date = [0] * 26

    for d in range(_to):

        now = schedule[d] + 1
        date[now - 1] = d + 1
        if d < _from:
            ret += satisfy[d]
            continue

        tmp = 0
        for i in range(26):
            tmp += c[i] * (d+1 - date[i])
        ret += tmp
        satisfy[d] = tmp

    return ret

def Main():
    D = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(D)]
    
    dissatisfy=[]
    schedule = []
    ans = search(D, schedule, c, s, dissatisfy)
    for i in range(D):
        print(schedule[i] + 1)


if __name__ == "__main__":
    Main()
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
        if d < _from-1:
            ret += satisfy[d]
            continue

        now = schedule[d] + 1
        date[now - 1] = d + 1
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
    score = 0
    start = time.time()

    #最大値を足すだけ
    # for i in range(D):
    #     schedule.append(np.argmax(s[i]))
    #     score += np.max(s[i])
    ans = search(D, schedule, c, s, dissatisfy)
    for i in range(D):
        score+=s[i][schedule[i]]
    
    while time.time() - start < 1.8:
        contest = random.randint(0, 25)
        day = random.randint(0, D - 1)
        if schedule[day] == contest:
            continue

        save = dissatisfy.copy()
        dec2 = change(day + 1, D, schedule, c, s, dissatisfy)
        score2 = score - s[day][schedule[day]] + s[day][contest]

        if ans < score2 - dec2:
            ans = score2 - dec2
            score = score2
            schedule[day] = contest
        else:
            dissatisfy = save

    for i in range(D):
        print(schedule[i] + 1)

if __name__ == "__main__":
    Main()

import random
import time

def search(day, c, s):
    schedule = []
    satisfy = []
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
        
        satisfy.append(tmp - c[contest] * (d + 1 - date[contest]))
        date[contest] = d + 1
        schedule.append(contest)
        score += s[d][contest] - satisfy[d]

    return score, schedule, satisfy

def change(day, contest,D, c, s, schedule, satisfy):
    ret = 0
    date = [0] * 26

    for d in range(D):
        if d == day:
            now = contest + 1
            date[now - 1] = d + 1
        else:
            now = schedule[d] + 1
            date[now - 1] = d + 1
        if d < day:
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
    c = tuple(map(int, input().split()))
    s = [tuple(map(int, input().split())) for _ in range(D)]
    
    dissatisfy=[]
    schedule = []
    score = 0
    start = time.time()

    ans, schedule, dissatisfy = search(D, c, s)
    
    for i in range(D):
        score += s[i][schedule[i]]

    while time.time() - start < 1.95:
        contest = random.randint(0, 25)
        day = random.randint(0, D - 1)
        if schedule[day] == contest:
            continue

        save = dissatisfy.copy()
        dec2 = change(day,contest,D,c, s, schedule, dissatisfy)
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
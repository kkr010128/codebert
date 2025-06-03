from time import time
start = time()

import random


def solve(c_list, days, now):
    r = sum(c_list[i]*(now-days[i]) for i in range(26))
    return r


d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _i in range(d)]


last_days = [-1 for _i in range(26)]
result = []
score = 0
for today in range(d):
    checker = [c[j]*(today-last_days[j]) for j in range(26)]
    y = sum(checker)

    finder = [s[today][j]-(y-checker[j]) for j in range(26)]
    x = finder.index(max(finder))

    last_days[x] = today
    result.append(x+1)
    score += s[today][x] - solve(c, last_days, today)


def change(problems, days):
    last_days = [-1 for _i in range(26)]
    score = 0
    for i in range(d):
        score += s[i][problems[i]-1]
        last_days[problems[i]-1] = i
        score -= sum([c[j]*(i-last_days[j]) for j in range(26)])
    return score

change_list = result.copy()
hantei = True
coun = 0
while hantei:
    if random.randrange(2)<1:
        x, y = random.randrange(0, d), random.randrange(0, d)
        while x == y:
            y = random.randrange(0, d)
        change_list[x], change_list[y] = change_list[y], change_list[x]
        next_score = change(change_list, d)
        if next_score >= score:
            score = next_score
            result[x], result[y] = result[y], result[x]
        elif random.randrange(100)==5:
            score = next_score
            result[x], result[y] = result[y], result[x]
        else:
            change_list[x], change_list[y] = change_list[y], change_list[x]
    else:
        x = random.randrange(0, d)
        y = random.randrange(1, 27)
        while change_list[x] == y:
            x = random.randrange(0, d)
            y = random.randrange(1, 27)    
        change_list[x], z = y, change_list[x]
        next_score = change(change_list, d)
        if next_score >= score:
            score = next_score
            result[x] = y
        else:
            change_list[x] = z
    coun += 1
    if coun ==100:
        coun = 0
        if time()-start >= 1.8:
            hantei = False

for i in result:
    print(i)
import sys
import random
test = False

def solve(c_list, days, now):
    r = sum(c_list[i]*(now-days[i]) for i in range(26))
    return r


if test == True:
    seed = 94
    random.seed(seed)
    d = 365
    c = [random.randrange(0, 101) for _ in range(26)]
    s = [[random.randrange(0, 20001) for _ in range(26)] for _ in range(d)]
    c_ = ' '.join(map(str, c))
    s_ = '\n'.join([' '.join(map(str, i)) for i in s])
    with open('./input.txt', 'w') as f:
        f.write('\n'.join([str(d), c_, s_]))
else:
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
#print(score)


if test == True:
    with open('./output.txt', 'w') as f:
        f.write('\n'.join(map(str, result)))
else:
    for i in result:
        print(i)
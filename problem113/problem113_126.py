import time, random
now = time.time()

d = int(input())
clst = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
last = [0 for _ in range(26)]

def score_minus(d, q):
    minus = 0
    for i, (c, ls) in enumerate(zip(clst, last)):
        if i == q:
            continue
        minus += c * (d + 1 - ls)
    return minus

def check(t):
    def score_minus(d):
        minus = 0
        for c, ls in zip(clst, last):
            minus += c * (d - ls)
        return minus
        
    last = [0 for _ in range(26)]
    ans = 0
    for d, num in enumerate(t, start = 1):
        ans += s[d - 1][num - 1]
        last[num - 1] = d
        ans -= score_minus(d)
    return ans
    
t_lst = []
for i in range(d):
    tmp = -10 ** 10
    for q in range(26):
        tmp_score = s[i][q] - score_minus(i, q)
        if tmp_score > tmp:
            tmp = tmp_score
            max_q = q
    last[max_q] = i
    t_lst.append(max_q + 1)

ans = check(t_lst)

while time.time() - now < 1.8:
    d_change = random.randint(0, d - 1)
    q_change = random.randint(1, 26)
    old_d = t_lst[d_change]
    if old_d == q_change:
        continue
    t_lst[d_change]  = q_change
    ans_tmp = check(t_lst)
    if ans_tmp > ans:
        ans = ans_tmp
    else:
        t_lst[d_change] = old_d

for t in t_lst:
    print(t)

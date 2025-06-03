import math


def f(n):
    pop = 0
    ntemp = n
    for i in range(int(math.log2(n)) + 1):
        pop += ntemp % 2
        ntemp //= 2
    return n % pop


n = int(input())
S = input()
popcount = 0
for i in range(n):
    popcount += int(S[i])

# 1が1個しかない場合の例外処理
if popcount == 1:
    if S[-1] == 1:
        ans = [2] * n
        ans[-1] = 0
    else:
        ans = [1] * n
        ans[-1] = 2
        for i in range(n):
            if S[i] == '1':
                ans[i] = 0
    for i in range(n):
        print(ans[i])
    exit()


Sint = int(S, 2)
remminus = Sint % (popcount - 1)
remplus = Sint % (popcount + 1)

# 1,2,4,...の余りのリストを準備
remlistminus = []
remlistplus = []
temp = 1
for i in range(n):
    remlistminus.append(temp)
    temp = (temp * 2) % (popcount - 1)
temp = 1
for i in range(n):
    remlistplus.append(temp)
    temp = (temp * 2) % (popcount + 1)
remlistminus.reverse()
remlistplus.reverse()

ans = []
for i in range(n):
    count = 1
    if S[i] == '0':
        rem = (remplus + remlistplus[i]) % (popcount + 1)
        while rem > 0:
            rem = f(rem)
            count += 1
    else:
        rem = (remminus - remlistminus[i]) % (popcount - 1)
        while rem > 0:
            rem = f(rem)
            count += 1
    ans.append(count)
for i in range(n):
    print(ans[i])

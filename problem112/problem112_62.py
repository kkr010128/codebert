#with open('random_pm00.txt') as f:
    #n, k = map(int, f.readline().split())
    #a = list(map(int, f.readline().split()))
n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

mia, pla = [], []
for ai in a:
    if ai < 0:
        mia.append(ai)
    elif ai >= 0:
        pla.append(ai)
mia.sort(reverse=True)
pla.sort()

cnt = 1
if len(pla) == 0 and k % 2 == 1:
    for i in mia[:k]:
        cnt = cnt * i % mod
else:
    while k > 0:
        if k == 1 or len(mia) <= 1:
            if len(pla) == 0:
                cnt = cnt * mia.pop() % mod
            elif len(pla) > 0:
                cnt = cnt * pla.pop() % mod
            k -= 1
        elif len(pla) <= 1:
            if k == 1:
                cnt = cnt * pla.pop() % mod
                k -= 1
            elif k > 1:
                cnt = cnt * mia.pop() * mia.pop() % mod
                k -= 2
        elif len(pla) >= 2 and len(mia) >= 2:
            if pla[-1] * pla[-2] > mia[-1] * mia[-2]:
                cnt = cnt * pla.pop() % mod
                k -= 1
            elif pla[-1] * pla[-2] <= mia[-1] * mia[-2]:
                cnt = cnt * mia.pop() * mia.pop() % mod
                k -= 2
print(cnt)

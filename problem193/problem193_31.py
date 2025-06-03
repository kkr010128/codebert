from itertools import product


def makelist(BIT):
    LIST, tmp = [], s[0]
    for i, bi in enumerate(BIT, 1):
        if bi == 1:
            LIST.append(tmp)
            tmp = s[i]
        elif bi == 0:
            tmp = [t + sij for t, sij in zip(tmp, s[i])]
    else:
        LIST.append(tmp)
    return LIST


def solve(LIST):
    CNT, tmp = 0, [li[0] for li in LIST]
    if any(num > k for num in tmp):
        return h * w
    for j in range(1, w):
        cal = [t + li[j] for t, li in zip(tmp, LIST)]
        if any(num > k for num in cal):
            CNT += 1
            tmp = [li[j] for li in LIST]
        else:
            tmp = cal
    return CNT


h, w, k = map(int, input().split())
s = [[int(sij) for sij in input()] for _ in range(h)]

ans = h * w
for bit in product([0, 1], repeat=(h - 1)):
    numlist = makelist(bit)
    ans = min(ans, solve(numlist) + sum(bit))
print(ans)
